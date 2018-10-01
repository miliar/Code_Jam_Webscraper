#!/usr/bin/python
import string, sys

def gcd(a, b):
    while a:
        a, b = b%a, a
    return b

nr = string.atoi(sys.stdin.readline().strip())
for i in range(nr):
    t = map(lambda x: string.atoi(x), sys.stdin.readline().strip().split()[1:])
    t.sort()
    tmin = t[0]
    v = map(lambda x: x-tmin, t[1:])
    g = reduce(gcd, v)
    y = g*((tmin + g - 1) // g) - tmin
    print 'Case #%d: %d' % (i + 1, y)
