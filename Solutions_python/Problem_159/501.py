#!/usr/bin/python
import sys

def getnums(fh):
    return [int(x) for x in fh.readline().split()]

def getstrings(fh):
    return [x for x in fh.readline().split()]

fh = open(sys.argv[1])

t, = getnums(fh)
for i in range(t):
    n, = getnums(fh)
    seg = getnums(fh)
    big = diff = suma = sumb = 0
    for j in range(n):
        if j > 0:
            diff = prev - seg[j]
            big = max(big, diff)
            if diff > 0:
                suma += diff
        prev = seg[j]
    for j in range(n-1):
        sumb += min(seg[j], big)
    print "Case #%d: %d %d" % (i+1, suma, sumb)
