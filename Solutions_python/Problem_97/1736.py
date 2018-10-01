#!/usr/bin/python
import sys
T=input()
for nin in range(T):
    line=sys.stdin.readline()
    n1=int(line.split(" ")[0])
    n2=int(line.split(" ")[1][:-1])
    length=len(str(n1))
    count=0
 
    if(n1>=n2):
        count=0
        sys.stdout.write("Case #"+str(nin+1)+": "+str(count)+"\n")
        continue
    for x in xrange(n1,n2,1):
        l=[]
        for y in range(length):
            x1=str(x)
            z=x1[y:]+x1[:y]
            if z[0]=="0":
                continue;
            z=int(z);
            iwc=0
            for i in l:
                if i==z:
                    iwc=1
                    continue
            if iwc==1:
                continue
          
            l.append(z)
            if z>x and z<=n2:
                count=count+1
    sys.stdout.write("Case #"+str(nin+1)+": "+str(count)+"\n")
            
            
    
