#!/usr/bin/env python

import sys

T = int(sys.stdin.readline().strip())

def next (N):
    last = len(N)-1
    digits = [-1]*10
    for i in range(last, 0, -1):
        digits[N[i]] = i
        for j in range(N[i-1]+1, 10):
            if digits[j] >= 0:
#                print 'j', j, 'i', i, 'd', digits
                k = digits[j]
                tmp = N[i-1]
                N[i-1] = N[k]
                N[k] = tmp
                N[i:] = sorted(N[i:])
                return N
    nzeros = len([i for i in N if i==0])
    nzeros = N.count(0)
    N = [i for i in N if i]
    N.sort()
    N = [N[0]] + [0]*(nzeros+1) + N[1:]
    return N

for t in xrange(T):

    N = sys.stdin.readline().strip()
#    N = '11222'
    N = [int(c) for c in N]
    digits = sorted([i for i in N if i != 0])

#    nn = N
#    print nn
#    while nn:
    nn = next(N)
#     print ''.join(str(c) for c in nn)


    print "Case #%d:" % (t+1), ''.join(str(c) for c in nn)

