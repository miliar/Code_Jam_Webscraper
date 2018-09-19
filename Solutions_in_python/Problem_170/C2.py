#!/usr/bin/python

from __future__ import division
from gcj import *

# boolean flags, reachable via OPTS.flagname. Space separated in string
FLAGS = ''

class O(object): pass

def case():
    N, = ints()
    lines = []
    for i in range(N):
        lines.append(line().split())

    D = {}
    for L in lines:
        for i in range(len(L)):
            if L[i] in D:
                L[i] = D[L[i]]
            else:
                d = len(D)
                D[L[i]] = d
                L[i] = d

    best = 1e1000
    A = [0] * len(D)
    B = [0] * len(D)

    m = O()

    def add(w, L):
        for i in L:
            w[i] += 1
    def rm(w, L):
        for i in L:
            w[i] -= 1
    def mv(f, t, L):
        for i in L:
            m.tot -= bool(f[i] and t[i])
            f[i] -= 1
            t[i] += 1
            m.tot += bool(f[i] and t[i])

    m.min = 1e100

    add(A, lines[0])
    add(B, lines[1])
    for i in range(2, N):
        add(A, lines[i])

    totaal = 0
    for i in range(len(D)):
        if A[i] and B[i]:
            totaal += 1

    m.tot = totaal

    def recur(depth):
        if depth == N:
            m.min = min(m.tot, m.min)
            return
        recur(depth+1)
        mv(A, B, lines[depth])
        recur(depth+1)
        mv(B, A, lines[depth])

    recur(2)

    return m.min

if __name__ == '__main__':
    main()
