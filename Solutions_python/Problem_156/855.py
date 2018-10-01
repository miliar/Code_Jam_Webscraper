t=input()
for x in range(0,t):
    n=input()
    a=map(int,raw_input().split())
    m=max(a)
    m1=m
    for i in range(1,m+1):
        s=i
        for j in range(0,n):
            if a[j]>i:
                if a[j]%i==0:
                    s+=((a[j]/(i))-1)
                else:
                    s+=a[j]/i
        m1=min(m1,s)
    r=m1
    print "Case #%d: %d" %(x+1,r)

