import collections, sys

lines = sys.stdin.readlines()
n = int(lines[0]) + 1

for _ in xrange(1, n):
    a, b = map(int, lines[_].split(' '))
    seen = dict(map(lambda x: (x, False), xrange(a, b + 1)))
    count = 0

    for i in xrange(a, b + 1):
        si = str(i)
        d = collections.deque(list(si))
        l = len(si)
        p = 0
        t = -1
        m = int(''.join(d))
        r = m
        if seen[m]: continue
        for j in xrange(l):
            d.rotate(1)
            n = int(''.join(d))
            has_seen = seen.get(n)
            if has_seen or has_seen is None: continue
            seen[n] = True
            if a <= n <= b and m != n:
                p += 1
                t += 1
            m = n
            if p > 1: count += t
    print 'Case #%d: %d' % (_, count)
