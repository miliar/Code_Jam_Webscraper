import psyco
psyco.full()

import sys, copy


def calc(R,k,N,groups):
    m = 0
    for ri in xrange(R):
        rp = 0
        rg = []
        while rp < k and len(groups) > 0:
            g = groups[0]
            if rp+g <= k:
                rp += g
                groups.pop(0)
                rg.append(g)
            else:
                break
        groups.extend(rg)
        m += rp
    return m



def inGen():
    for line in open(sys.argv[1], 'r'):
        yield line.strip('\n')

ig = inGen()
ig.next()
cn = 1
for line in ig:
    R,k,N = [int(s) for s in line.split(' ')]
    line2 = ig.next()
    groups = [int(s) for s in line2.split(' ')]
    
    print "Case #%d: %s" % (cn,calc(R,k,N,groups))
    cn += 1

