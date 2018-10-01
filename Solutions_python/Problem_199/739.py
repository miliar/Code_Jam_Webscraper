#!/bin/python

def solve(s, k):
    l = list(s)
    f = 0
    while True:
        if not l:
            return str(f)

        if l[0] == '+':
            l.pop(0)
            continue

        if len(l) < k:
            return 'IMPOSSIBLE'

        for i in xrange(k):
            l[i] = '+' if l[i] == '-' else '-'
        f += 1

    return 'IMPOSSIBLE'

n = int(raw_input())
for i in xrange(n):
    s, k = raw_input().split()
    k = int(k)
    print 'Case #%d: %s' % (i + 1, solve(s, k))

