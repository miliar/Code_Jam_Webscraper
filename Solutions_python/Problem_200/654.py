#!/usr/bin/python

import sys

def brute( S ):
    flipped = False
    out = ''
    i = 0
    while i < len( S):
        if flipped:
            S[i] = 9
            i = i + 1
            continue
        if i > 0 and S[i] < S[i-1]:
            flipped = True
            while i > 0 and S[i] < S[i-1]:
                S[i-1] = S[i-1] - 1
                i = i - 1
            i = i + 1
            continue
        i = i + 1
    if S[0] == 0:
        S.pop(0)
    return ''.join([str(x) for x in S])

data = file(sys.argv[1]).read().splitlines()

NUMCASE = int(data.pop(0))

for CASE in xrange( 1, NUMCASE + 1 ):
    print 'Case #%d:' % ( CASE, ),
    S = data.pop(0)
    S = [int(x) for x in list(S)]
    print brute( S )

        
