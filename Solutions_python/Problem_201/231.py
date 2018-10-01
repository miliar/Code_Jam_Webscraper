#!/usr/bin/env python3
from collections import Counter

# have the gards some kind of diarrhea ?

# N is an integer
def cut(N):
    "give the (L_S, R_S) attributes for the optimal stall among N consecutive empty stalls"
    N -= 1
    return (N//2, N-N//2)

# somes rules :
# let M <= N
# we have :
# L_S(M) <= R_S(M)   (cf. the leftmost rule ; delta in [0,1])
# L_S(M) <= L_S(N)   (cf. min rule)
# R_S(M) <= R_S(N)   (cf. max rule)


# N is an integer (or a Counter designating the number of ranges of N empty stalls)
# K is an integer
def fill(N, K):
    "fill all stalls one by one and return (L_S, R_S) of the last iteration"
    if isinstance(N, int): N = Counter({N:1})
    while K > 0:
        gap = max(N)
        k = N.pop(gap) # k people allowed to choose a stall at the same time
        LR_S = cut(gap)
        for S in LR_S:
            N[S] += k
        K -= k
    return LR_S

import sys
file=sys.stdin

n = int(file.readline()) # number of cases
for i in range(1, n+1):
    N, K = [int(n) for n in file.readline().split()]

    L_S, R_S = fill(N, K)

    print("Case #%d: %s %s" % (i, R_S, L_S))
