#!/usr/bin/env python2

import sys
p = sys.stdin
for t in range(int(p.readline())):
    v = set(range(1, 16 + 1))
    for x in range(2):
        q = int(p.readline())
        ls = [p.readline() for _ in range(4)]
        ls = ls[q - 1][:-1].split(' ')
        v = v.intersection([int(x) for x in ls])

    if len(v) == 0:
        out = 'Volunteer cheated!'
    elif len(v) == 1:
        out = v.pop()
    else:
        out = 'Bad magician!'
    print 'Case #%d: %s' % (t + 1, out)
