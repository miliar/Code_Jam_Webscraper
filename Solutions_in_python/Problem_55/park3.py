#!/usr/bin/env python

import fileinput

def main():
    reader = fileinput.input()
    cases = int(reader.next())
    for case in range(1, cases+1):
        r, k, n = [int(x) for x in reader.next().split()]
        g = [int(x) for x in reader.next().split()]
        assert len(g) == n
        print "Case #%d: %d" % (case, park(r, k, g))

def park(r, k, g):
    prefix, p, cycle = findcycle(k, g)
    if r < prefix['rides']:
        return count(0, r, k, g)
    r -= prefix['rides']
    e = prefix['euros']
    if cycle['rides'] < r:
        n = r // cycle['rides']
        e += n * cycle['euros']
        r -= n * cycle['rides']
    return e + count(p, r, k, g)

def count(p, r, k, g):
    euros = 0
    for _ in range(r):
        e, p = fill(p, k, g)
        euros += e
    return euros

def findcycle(k, g):
    visited = [False] * len(g)
    p = 0
    r = 0
    eu = 0
    while not visited[p]:
        visited[p] = (r, eu)
        e, p = fill(p, k, g)
        eu += e
        r += 1
    return {
        'rides': visited[p][0],
        'euros': visited[p][1]
        }, p, {
        'rides': r - visited[p][0],
        'euros': eu - visited[p][1]
        }

def fill(p, k, g):
    e = 0
    p0 = p
    while e + g[p] <= k:
        e += g[p]
        p = (p + 1) % len(g)
        if p == p0:
            break
    return e, p

main()
