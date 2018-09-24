#!/usr/bin/env python

from sys import stdin

n = int(stdin.readline())

for case in xrange(n):
    n_e = int(stdin.readline())
    engines = {}
    for engine in xrange(n_e):
        engines[stdin.readline()[:-1]] = engine

    n_s = int(stdin.readline())
    searches = []
    for _ in xrange(n_s):
        query = stdin.readline()[:-1]
        if query in engines:
            searches.append(engines[query])
        else:
            searches.append(-1)

    results = [9999]*(n_s + 1)
    results[n_s] = 0

    for i in xrange(n_s-1, -1, -1):
        for j in xrange(n_e):
            if searches[i] != j:
                results[i] = min(results[i], results[i+1]+1)
                for k in xrange(i+1, n_s):
                    if searches[k] != j:
                        results[i] = min(results[i], results[k+1]+1)
                    else:
                        break

    if n_s == 0:
        results[0] = 1
    print 'Case #%d: %d' % (case+1, results[0]-1)
