def inparr():
    return map(int,raw_input().strip().split())


for tc in xrange(1,1+input()):
    print 'Case #%d:'%tc,
    n,p=inparr()
    g=inparr()
    a = [0]*p
    for i in g:
        x = i%p
        a[x]+=1
    ans = a[0]
    a[0]=0
    if p==4:
        m=min(a[1],a[3])
        ans+=m
        a[1]-=m
        a[3]-=m
        a[3]=max(a[1],a[3])
        m=min(a[2],a[3]/2)
        ans+=m+(a[3]-2*m)/4+(a[2]-m)/2+int(bool(a[3]+a[2]-3*m))
    if p==2:
        ans+=a[1]/2+a[1]%2
    if p==3:
        ans+=min(a[1],a[2])
        a[1],a[2]=0,abs(a[1]-a[2])
        ans+=(a[2]+2)/3
    print ans
