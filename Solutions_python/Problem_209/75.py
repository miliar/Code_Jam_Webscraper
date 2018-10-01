import os
import math

from decimal import Decimal, getcontext

getcontext().prec = 23

def g(k,l):
    if k > len(l): return -1
    r0,h0 = l[0]
    ll = [h*r for r,h in l[1:]]
    ll.sort(reverse=True)
    return r0*r0 + 2*r0*h0 + 2*sum(ll[:k-1])

def solve(n,k,l):
    l.sort(reverse=True)
    ma = -1
    for i in xrange(n):
        # print i, g(k,l[i:])
        ma = max(ma, g(k,l[i:]))
    res = Decimal('3.14159265358979323846') * ma
    return res

with open(os.path.expanduser("~/PycharmProjects/gcj/2017/1C/A.in")) as f:
    m = int(f.readline().strip('\n'))
    # print m
    for i in range(m):
        n,k = [int(x) for x in f.readline().strip().split()]
        l = []
        for j in xrange(n):
            r,h = [int(x) for x in f.readline().strip().split()]
            l.append((r,h))
        res = solve(n,k,l)
        print 'Case #' + str(i+1) + ': ' + str(res)