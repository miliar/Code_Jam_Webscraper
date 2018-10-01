#! /usr/bin/env python

import sys

c = {"O": 0, "B": 1}
for i in xrange(int(sys.stdin.readline())):
    a = [c[x] if x in c else int(x) for x in sys.stdin.readline().strip().split(" ")]
    t, x0, t0 = 0, [1, 1], [0, 0]
    for j in xrange(a[0]):
        k, x = a[1::2][j], a[2::2][j]
        dt = max(abs(x - x0[k]) - t0[k], 0) + 1
        t += dt
        x0[k], t0[k] = x, 0
        t0[1 - k] += dt
    print "Case #%d: %d" % (i + 1, t)

# [EOF]
