T = int(raw_input())

for x in xrange(1,T+1):
    str = list(raw_input())
    l = []
    
    for c in str:
        if c not in l:
            l.append(c)
    k = []
    k.append(1)
    k.append(0)
    t = 2
    while len(k)<len(l):
        k.append(t)
        t+=1       

    str.reverse()     
    base = len(k)
    i = 1
    t = 0
    for y in str:
        t+=i*k[l.index(y)]
        i*=base
    print "Case #%d: %d"%(x,t)

