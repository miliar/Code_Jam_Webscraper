from math import *
import sys

def getnum():
    return [int(x) for x in sys.stdin.readline().split()]

def gcd(x,y):
    while x:
        x, y = y % x, x
    return y

def gcda(x):
    r = x[0]
    for i in x:
        r = gcd(r, i)
    return r

C, = getnum()
for c in range(1, C+1):
    tmp = getnum()
    N = tmp[0]
    t = tmp[1:]
    gcdr = 0

    t.sort()

    for i in range(N-1):
        d = t[i+1]-t[i]
        if gcdr == 0:
            gcdr = d
        else:
            gcdr = gcd(gcdr, d)

    if gcdr == 1:
        result = 0
    else:
        if t[0] % gcdr == 0:
            result = 0
        else:
            result = gcdr - (t[0] % gcdr)

    print "Case #%d: %d" % (c, result)
