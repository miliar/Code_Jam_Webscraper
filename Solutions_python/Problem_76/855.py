"""C
   Google CodeJam 2011
"""

from datetime import datetime
from itertools import combinations
import operator


def routine(N, C):
    #sc = set(C)
    sc = C
    best = 0
    for p in xrange(len(C)/2):
        for c in combinations(C, p+1):
            rest = C[:]
            for x in c:
                rest.remove(x)
            fake = reduce(operator.xor, rest)
            #print c, rest, sum(c), fake
            if sum(c) == fake:
                test = sum(rest)
                if test > best:
                    best = test
    
    return best if best else "NO"

if __name__ == '__main__':
    filename = "C-small-attempt1"
    f = open(filename + ".in")
    fo = open(filename + ".out", "w")

    print datetime.now()

    c = int(f.readline().strip())
    print c, "cases"
    for case in xrange(c):
        N = [int(x) for x in f.readline().split()]
        C = [int(x) for x in f.readline().split()]
        print N, C

        print >>fo, "Case #%d: %s" % (case+1, routine(N, C))

    fo.close()
    f.close()
    print datetime.now()
