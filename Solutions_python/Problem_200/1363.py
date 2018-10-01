#!/usr/bin/env python3

T = int(input())

for t in range(1, T+1):
    S = list(input())
    S.reverse()
    S = [ int(s) for s in S ]
    l = len(S)
    
    ncnt = 0
    npos = -1
    for i in range(l-1):
        if S[i+1] > S[i]:
            npos = i
            S[i+1] -= 1
    for i in range(npos+1):
        S[i] = 9
    S.reverse()
    print("Case #{0}: {1}".format(t, int(''.join([ str(d) for d in S ]), 10)))
