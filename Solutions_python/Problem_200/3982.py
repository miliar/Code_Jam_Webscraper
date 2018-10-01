#!/usr/bin/env python

f = open('/dev/stdin', 'r')

def is_tidy(n):
    return n == ''.join(sorted(n))

N = int(f.readline())

i = 1
for _ in range(N):
    t = map(int, f.readline().strip())

    while not is_tidy(''.join(map(str, t))):
        for p in xrange(len(t) - 2, -1, -1):
            if t[p] > t[p + 1]:
                t[p] -= 1
                for p2 in xrange(p + 1, len(t)):
                    t[p2] = 9
                break

    print('Case #%d: %s' % (i, ''.join(map(str, t)).lstrip('0')))

    i += 1
