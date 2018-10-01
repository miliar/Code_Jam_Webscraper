#!/opt/local/bin/python

"""Premature optimization is the root of all evil."""

import sys
import re

DBG = False

def floydwarshall(D):
    if DBG:
        [print(x) for x in D]
        print("^"*80)
    dist = [[float('inf') for _ in range(len(D))] for _ in range(len(D))]
    for v in range(len(D)):
        dist[v][v] = 0
    for x in range(len(D)):
        for y in range(len(D)):
            dist[x][y] = D[x][y]
    if DBG:
        [print(x) for x in dist]
        print("~"*80)
    for k in range(len(D)):
        for i in range(len(D)):
            for j in range(len(D)):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    if DBG:
        [print(x) for x in dist]
        print("="*80)
    return dist





def doit(H, D, Q):
    for x in range(len(D)):
        for y in range(len(D)):
            if D[x][y] == -1:
                D[x][y] = float('inf')

    geography = floydwarshall(D)
    
    tim = [[float('inf') for _ in range(len(D))] for _ in range(len(D))]

    for x in range(len(D)):
        for y in range(len(D)):
            if geography[x][y] <= H[x][0]:
                if geography[x][y] / H[x][1] < tim[x][y]:
                    tim[x][y] = geography[x][y] / H[x][1]

    letsgo = floydwarshall(tim)
    out = [letsgo[a][b] for (a, b) in Q]
    return out


T = int(sys.stdin.readline())
for casenum in range(T):
    (N, Q) = [int(x) for x in sys.stdin.readline().split()]
    H = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
    D = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
    Qs = [[int(x)-1 for x in sys.stdin.readline().split()] for _ in range(Q)]

    n = [str(x) for x in doit(H, D, Qs)]




    print("Case #" + str(casenum + 1) + ": " + " ".join(n) )
