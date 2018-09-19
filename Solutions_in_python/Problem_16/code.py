# use Py2.6!

import sys, itertools

def proc(k, cad):
    licad = [None]* len(cad)
    lencorta = sys.maxint

    for perm in itertools.permutations(xrange(k)):
#        print perm
        base = 0
        for kk in xrange(len(cad)/k):
            for i,p in enumerate(perm):
                licad[base+i] = cad[base+p]
            base += k
#        print licad
            
        largo = 0
        ant = None
        for let in licad:
            if let != ant:
                ant = let
                largo += 1
#        print largo
        if largo < lencorta:
            lencorta = largo
    return lencorta
                


archinp = open(sys.argv[1])
canttests = int(archinp.readline())

for numtest in xrange(1,canttests+1):
    k = int(archinp.readline().strip())
    cadena = archinp.readline().strip()
    largo = proc(k, cadena)
    print "Case #%d: %d" % (numtest, largo)
    sys.stdout.flush()
