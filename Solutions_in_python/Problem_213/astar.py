def inparr():
    return map(int,raw_input().strip().split())


for tc in xrange(1,1+input()):
    print 'Case #%d:'%tc,
    n,c,r=inparr()
    c1 = []
    c2 = []
    for i in xrange(r):
        a,b = inparr()
        if b==1:
            c1.append(a)
        else:
            c2.append(a)
    prom=0
    mf1=2
    mf2=2
    dct = {}
    l1 = len(c1)
    l2 = len(c2)
    e1,e2=[c1.count(1),c2.count(1)]
    ans = max(l1,l2,e1+e2)
    if e1+e2==ans:
        print ans, 0
        continue
    air1,air2=0,0
    for i in xrange(2,1+n):
        a,b=[c1.count(i),c2.count(i)]
        if l1-a<b and l2-b<a:
            prom+=min(b+a-l1,b+a-l2)
    print ans,prom
    '''
        if a<b:
            if e2>=a:
                e2-=a
                e1+=b
            elif e1>=b:
                e1-=b
                e2+=a
            else:
                air1=a-e2
                air2=b-e1
                e1=0
                e2=0
        else:
            if e1<b:
                e2-=a
                e1+=b
            else:
                e1-=b
                e2+=a
'''
