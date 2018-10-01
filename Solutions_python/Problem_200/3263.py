import sys

test=int(input().strip())
for i in range(test):
    num=int(input().strip())
    g=[]
    g=str(num)
    x=[]
    for digits in g:
        x.append(int(digits))   
    b=len(x)
    y=len(x)
    b=b-1
    t=""
    while b>0:
        if x[b]<x[b-1]:
            x[b-1]=x[b-1]-1
            j=b
            while(j<y):
                x[j]=9
                j=j+1
        b=b-1

    p=0
    if x[p]==0:
        p=p+1
        
    while p<y:
        t=t+str(x[p])
        p=p+1
    print("Case #"+str(i+1)+": "+t)    
    
    
