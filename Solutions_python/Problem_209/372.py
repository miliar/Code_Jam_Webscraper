from itertools import combinations as cmb
from math import pi
import sys

def read():
    return map(int, raw_input().strip().split())

def small(n, k, cakes):
    maxArea = 0
    for c in cmb(cakes, k):
        ht = 0
        rmax = 0
        for cake in c:
            ht += cake[0]*cake[1]
            rmax = max(cake[0], rmax)
        maxArea = max( pi*(ht*2 + rmax**2), maxArea)
    return maxArea

for i in range(input()):
    N, K = read()
    cakes = []
    for c in range(N):
        cakes.append(read())
    print "Case #{}: {:f}".format(i+1, small(N, K, cakes))
    print >> sys.stderr, "Case #{}: {:f}".format(i+1, small(N, K, cakes))
