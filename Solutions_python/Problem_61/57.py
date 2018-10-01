"""C
   Google CodeJam 2010
"""

from datetime import datetime
from itertools import combinations

cache = {}

def pure(s, n):
    if n not in s:
        return False
    so = list(s)
    so.sort()
    while n in so:
        n = so.index(n) +1
        if n == 1:
            #print "TRUE"
            return True
    if n == 1:
        return True
    return False

def routine(n):
    if n in cache:
        return cache[n]
    
    count = 0
    
    for ssize in xrange(n):
        if ssize > 0:
            for ss in combinations(xrange(2, n+1), ssize):
                #print ss
                if pure(ss, n):
                    count += 1
    
    cache[n] = count % 100003
    return count % 100003

if __name__ == '__main__':
    filename = "C-small-attempt1"  #small-attempt0 large
    f = open(filename + ".in")
    fo = open(filename + ".out", "w")

    print datetime.now()

    c = int(f.readline().strip())
    print c, "cases"
    for case in xrange(c):
        n = int(f.readline().strip())
        print n
        
        print >>fo, "Case #%d: %s" % (case+1, routine(n))

    fo.close()
    f.close()
    print datetime.now()
