#!/usr/bin/python

import os
import sys

fin = sys.stdin

def follow(G, n, i, p):
    P = G[p]
    #if (n, i) not in P:
    P[1].append((n, i))
    for np in P[0]:
        follow(G, n, p, np)

def isRootDiamond(G, n):
    tmp = {}
    for c, i in G[n][1]:
        if c not in tmp:
            tmp[c] = [i]
        else:
            if i not in tmp[c]:
                return True

def main():
    T = int(fin.readline())
    for t in xrange(1, T + 1):
        N = int(fin.readline())
        G = {}
        for n in xrange(1, N + 1):
            l = map(int, fin.readline().strip().split())
            G[n] = (l[1:], [])
        for n in G:
            for p in G[n][0]:
                follow(G, n, n, p)
        root = False
        for n in G:
            if isRootDiamond(G, n):
                root = True
        
        if root:
            msg = 'Yes'
        else:
            msg = 'No'

        print 'Case #%d: %s' % (t, msg)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fin = open(sys.argv[1], 'r')
    main()
