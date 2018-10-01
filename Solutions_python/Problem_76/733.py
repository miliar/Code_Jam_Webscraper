import psyco
psyco.full()

import math, itertools, sys

def xorl(s):
    x = 0
    for n in s:
        x ^= n
    return x

#def patrick_add(a,b):
#    return a^b
#            
#def cc(n,k):
#    f = math.factorial
#    return f(n) / (f(k)*f(n-k))


def calc(ns):
    smax = 0
    for k in xrange(1,len(ns)):
        for pa in itertools.combinations(ns,k):
            pb = list(ns)
            for n in pa:
                pb.remove(n)
            sa,sb = sum(pa),sum(pb)
            if sa>smax or sb>smax:
                if xorl(pa) == xorl(pb):
                    smax = max((sa,sb))
    if smax==0:
        return 'NO'
    else:
        return str(smax)
                

def inGen():
    for line in open(sys.argv[1], 'r'):
        yield line.strip('\n')

ig = inGen()
ig.next()

c = 1
for line in ig:
    line = ig.next()
    ns = [int(n) for n in line.split(' ')]
    print "Case #%d: %s" % (c,calc(ns))
    c += 1
