#code jam

t=int(input())
res1=[]
res2=[]
for i in range(0,t):
    n=int(input())
    k=int(input())
    a=[0,n+1]
    for l in range(0,k):
        max=0
        a.sort()
        for j in range(0,len(a)-1):
            if(max<a[j+1]-a[j]):
                max=a[j+1]-a[j]
                f=a[j]
                l=a[j+1]
        if((f+l)<=(n+2)):
            a.append(f+int(max/2))
        else:
            a.append(l-int(max/2))
    r=a[-1]
    a.sort()
    j=a.index(r)
    x=a[j]-a[j-1]-1
    y=a[j+1]-a[j]-1
    if(x>y):
        res1.append(x)
        res2.append(y)
    else:
        res1.append(y)
        res2.append(x)
        
for i in range (0,t):
    print("case #{0}: {1} {2}".format(i+1,res1[i],res2[i]))
