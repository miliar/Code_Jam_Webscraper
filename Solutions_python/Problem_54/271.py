def xl(l):
    return xrange(len(l))

def gcd(l):
    return reduce(gcdtwo,l)

def gcdtwo(a,b):
    while b:      
 	 a, b = b, a % b
    return a

for case in range(input()):
    print "Case #"+str(case+1)+":",
    #p=raw_input().split()
    t=map(int,raw_input().split()[1:])
    t.sort()
    #Tmax=min(t[i]-t[i-1] for i in xrange(1,len(t)))
    diffs=[t[i]-t[i-1] for i in xrange(1,len(t))]
    #for T in xrange(1,Tmax):
    #    mods=[(x%T) for x in t]
    #    #print T,mods,all(mods[0]==x for x in mods)
    #print max(T for T in xrange(1,Tmax) if all(t[0]%T==x%T for x in t))
    T=gcd(diffs)
    #print T
    if t[0]%T==0:
        print 0
    else:
        print T-(t[0]%T)
    #print [(x%T) for x in t]
