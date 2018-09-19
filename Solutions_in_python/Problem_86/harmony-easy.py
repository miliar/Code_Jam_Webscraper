#!/usr/bin/env python

from sys import stdin
from fractions import gcd

T = int(stdin.readline())


for CASO in xrange(1,T+1):
    (N, L, H) = [int(x) for x in stdin.readline().strip().split(" ")]
    P = [int(x) for x in stdin.readline().strip().split(" ")]

    ans = 0

    for i in xrange(L, H+1):
        bad = False

        for p in P:
            if (p % i) != 0 and (i % p) != 0:
                bad = True
                break

        if not bad:
            ans = i
            break

    if ans == 0:
        print "Case #%d: NO" % CASO
    else:
        print "Case #%d: %d" % (CASO, ans)
