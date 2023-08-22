print("============================");
x=[];
for r in range(1,1000):
   x.append(r);

z=[];
for i in range(1,2000):
    for a in x:
        if i%a==0 and (a==i or a==1):
         if i==1:
            continue;
         else:
            z.append(i);
    
print(z[0:9])
