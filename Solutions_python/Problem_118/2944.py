from math import sqrt
from math import floor


f = open('C-small-attempt0.in', 'r')
op=open('output.in','w')
i=0



for i,line in enumerate(f):
    if i==0:
        continue
    
    j=0
    a=0
    b=0
    fairnsq=[]
    pos=[]
    possible1=[]
    for x in line:
        if(j==0 and (ord(x)>47)):
            a=10*a+int(x)
        if x==' ':
            j=1
        if(j==1 and (ord(x)>47)):
            b=10*b+int(x)
       
    for n in range(a,b+1):
        if n==(floor(sqrt(n)))**2:
            possible1.append(n)
    print possible1
    for n in possible1:
            size=0
            temp=n
            n=int(sqrt(temp))
            print n,
            pal=[]
            while n>0:
                pal.append(n%10)
                size=size+1
                n=n/10
                j=0
            
            for c,t in enumerate(pal):
                if t!=pal[size-1-c]:
                    j=1
                    break
            if j==0:
                pos.append(temp) 
                
                   
    print pos
    for n in pos:
            size=0
            temp=n
            pal=[]
            while n>0:
                pal.append(n%10)
                size=size+1
                n=n/10
            j=0
            
            for c,t in enumerate(pal):
                if t!=pal[size-1-c]:
                    j=1
                    break
            if j==0:
                fairnsq.append(temp)
            
        
    
    op.write('Case #'+str(i)+': '+str(len(fairnsq))+'\n')
    
    

f.close()
op.close()

    
