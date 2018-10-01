from Allimports import *
t=int(input())
for q in range(t):
    d,n=[int(i) for i in input().split(' ')]
    di=dict()
    k=[]
    s=[]
    for i in range(n):
        i1,i2=[int(i) for i in input().split(' ')]
        k.append(i1)
        s.append(i2)
        di[i1]=i2
    #print(di)
    if(n==1):
        #print(type(d),type(k[0]),type(s[0]))
        print("Case #%d: %.6f"%(q+1,d/((d-k[0])/s[0])))
    elif(n==2):
        a=max(k[0],k[1])
        a1=sum(k)-a
        b=di[a]
        b1=di[a1]
        if(b1!=b):
            x=(b1*a-b*a1)/(b1-b)
            #print(x)
            t=0
            if(x<d):
               t=max((x-k[0])/s[0], (x-k[1])/s[1])
               t+=(d-x)/min(s[0],s[1])
               #print(t)
               print("Case #%d: %.6f"%(q+1,d/t))
            else:
                t = max((d - k[0]) / s[0], (d - k[1]) / s[1])
                print("Case #%d: %.6f" % (q + 1, d / t))
        else:
            t = max((d - k[0]) / s[0], (d - k[1]) / s[1])
            print("Case #%d: %.6f" % (q + 1, d / t))