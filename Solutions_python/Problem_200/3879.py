#!/usr/bin/env python

with open('B-large.in') as f:
    with open('B.out', 'w') as g:
        T = int(f.readline())
        for i in xrange(T):
            N = f.readline().strip()
            n = int(N)
            c = N[0]
            t = c * len(N)
            while int(t) > n:
                c = str(int(c) - 1)
                t = c * len(N)
            ti = c
            for j in xrange(len(N) - 1):
                c = str(int(ti[-1]) + 1)
                t = ti + c * (len(N) - j - 1)
                while int(t) <= n:
                    c = str(int(c) + 1)
                    t = ti + c * (len(N) - j - 1)
                ti += str(int(c) - 1)
            g.write('Case #%d: %d\n' % ((i+1), int(ti)))
