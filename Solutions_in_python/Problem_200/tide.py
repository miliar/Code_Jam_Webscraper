import sys

a=int(input().strip())
for i in range(a):
    b=int(input().strip())
    l=[]
    l=str(b)
    c=[]
    for digits in l:
        c.append(int(digits))   
    k=len(c)
    m=len(c)
    k=k-1
    a=""
    while k>0:
        if c[k]<c[k-1]:
            c[k-1]=c[k-1]-1
            j=k
            while(j<m):
                c[j]=9
                j=j+1
        k=k-1

    ck=0
    if c[ck]==0:
        ck=ck+1
        
    while ck<m:
        a=a+str(c[ck])
        ck=ck+1
    print("Case #"+str(i+1)+": "+a)    
    
    
