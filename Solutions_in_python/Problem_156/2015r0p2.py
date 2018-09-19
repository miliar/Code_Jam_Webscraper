import sys
input = sys.stdin.readline
from collections import deque
from bisect import bisect, insort
from itertools import count

for _ in xrange(int(input())):
    d = int(input())
    p = map(int, input().split())
    p.sort(reverse=True)
    p = deque(p)
    o = []
    m = 1e3000
    t = 0
    lm = p[0]
    while p or o:
        if not o or p and p[0] >= o[-1]:
            e = p.popleft()
        else:
            e = o.pop()
        k, j = 1e3000, 0
        b = max(p[0] if p else 0, o[-1] if o else 0)
        for i in xrange(2, max(e, 3)):
            n = max(b, (e + i - 1) // i) + t + i - 1
            if n < k:
                k, j = n, i
        f = e // j
        for i in xrange(e % j):
            insort(o, f + 1)
        for i in xrange(j - e % j):
            insort(o, f)
        m = min(m, e + t, max(p[0] if p else 0, o[-1] if o else 0) + t + j - 1)
        lm = max(p[0] if p else 0, o[-1] if o else 0) + t + j - 1
        t += j - 1
        while p and t >= p[-1]:
            p.pop()
        i = 0
        while i < len(o) and t >= o[i]:
            i += 1
        if i: o = o[i:]
    print 'Case #%d: %d' % (_+1, m)
