#!/usr/bin/python

import sys, re, string, math, fractions, itertools
from fractions import Fraction
import heapq

#Z = 10**9 + 7
ssr = sys.stdin.readline
ssw = sys.stdout.write
sew = sys.stderr.write
def rdline(): return ssr().strip()
def rdstrs(): return ssr().split()
def rdints(): return map(int, ssr().split())
def rd1int(): return int(rdline())




def minpath(adj, s, d):
    """Dijkstra min path from s to d
    adj is dict containing list of (neighbor, cost)
    Nodes can be anything with assignment and equality test
    Costs can be non-negative integer, float, fraction, ...
    Returns min cost or -99 if unreachable"""
    if s==d:
        return 0
    best = {}
    heap = [ (0, s) ]
    while heap and (d not in best or heap[0][0]<best[d]):
        y,x = heapq.heappop(heap)
        if x not in best or y<best[x]:
            best[x] = y
            if x in adj:
                for (z,c) in adj[x]:
                    heapq.heappush(heap, (y+c, z))
    return best.get(d, -99)


def minpathall(adj, s):
    """Dijkstra min path from s to all
    adj is dict containing list of (neighbor, cost)
    Nodes can be anything with assignment and equality test
    Costs can be non-negative integer, float, fraction, ...
    Returns min cost or -99 if unreachable"""
    best = {}
    heap = [ (0, s) ]
    while heap:
        y,x = heapq.heappop(heap)
        if x not in best or y<best[x]:
            best[x] = y
            if x in adj:
                for (z,c) in adj[x]:
                    heapq.heappush(heap, (y+c, z))
    return best




def do_one_case(cnum):
    N,Q = rdints()
    E = []
    S = []
    D = {}
    DD = {}
    for i in range(N):
        e, s = rdints()
        E.append(e)
        S.append(s)
    for i in range(N):
        d = rdints()
        assert len(d)==N
        dd = enumerate(d)
        D[i] = [ (j,k) for (j,k) in dd if k>0 ]
    #print D
    for i in range(N):
        b = minpathall(D, i)
        #print i, b
        d = []
        for j in b:
            if j != i and b[j]<=E[i]:
                d.append((j, float(b[j])/S[i]))
        DD[i] = d
    #print DD
    a = []
    for i in range(Q):
        U, V = rdints()
        U -= 1
        V -= 1
        t = minpath(DD, U, V)
        #print U, V, t
        a.append("%.9g" % (t,))
    print "Case #%d: %s" % (cnum, " ".join(a))


def main():
    T = rd1int()
    for i in range(T):
        do_one_case(i+1)
        sys.stdout.flush()


if __name__ == "__main__":
    main()
