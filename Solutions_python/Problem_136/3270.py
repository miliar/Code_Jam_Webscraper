from __future__ import division

import sys

big = 200000

t = int(sys.stdin.readline())
for z in range(t):
    c, f, x = [float(x) for x in sys.stdin.readline().split()]
    r = big
    s = 0
    q = 2

    while s + x / q < r:
        r = s + x / q
        s += c / q
        q += f

    print 'Case #{0}: {1}'.format(z + 1, r)
