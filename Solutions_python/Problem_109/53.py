import random
import math

def overlap(ps, rs):
    for i, (x1, y1) in enumerate(ps):
        for j in xrange(i+1, len(ps)):
            (x2, y2) = ps[j]
            dx = x1-x2
            dy = y1-y2
            if math.hypot(dx, dy) < rs[i] + rs[j]:
                return i, j
    return None

def solve(W, L, rs):
    while True:
        ps = [(random.random()*W, random.random()*L) for i in rs]
        if not overlap(ps, rs):
            return ps

T = int(raw_input())
for case in xrange(1, T+1):
    N, W, L = map(int, raw_input().split())
    rs = map(int, raw_input().split())
    ps = solve(W, L, rs)
    print 'Case #%i: %s' % (case, ' '.join((str(x) + ' ' + str(y) for x, y in ps)))
