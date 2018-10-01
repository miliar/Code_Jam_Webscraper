#!/usr/bin/env python

import itertools
import math

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def go(t):
    diffs = [abs(a-b) for (a, b) in itertools.combinations(t, 2)]
    ggcd = reduce(gcd, diffs)
    #print "ggcd(%s) = %d" % (str(diffs), ggcd)
    onev = max(t)
    #print "onev =", onev
    #print "ceil =", math.ceil(onev*1.0/ggcd)
    mmul = int(math.ceil(onev*1.0/ggcd))*ggcd
    while mmul < onev:
        mmul += ggcd
        #print "mmul =", mmul
    return mmul-onev



if __name__ == '__main__':
    import fileinput
    inp = fileinput.input()
    c = int(inp.readline())
    for i in xrange(c):
        t = map(int, inp.readline().split()[1:])
        print "Case #%d: %d" % (i+1, go(t))
