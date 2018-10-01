#!/usr/bin/python

import sys

i = iter(sys.stdin.read().split())

T = int(next(i))

for case in xrange(1,T+1):
    A, B = next(i), next(i)

    result = 0
    digits = len(A)

    for n in map(str, xrange(int(A), int(B))):
        nn = n + n
        result += len(set(m for m in (nn[s:s+digits] for s in xrange(1,digits)) if n < m <= B))

    print "Case #%d:" % case, result
