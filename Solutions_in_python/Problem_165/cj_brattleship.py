#!/usr/bin/python
# -*- coding: utf-8 -*-


def solve(r, c, w):
    if w == 1:
        return r * c
    if w == c:
        return r + w - 1
    if w > c / 2:
        return r + w
    if w == c / 2:
        return r + w + c % 2
    if c % w == 0:
        return r * (c / w) + w - 1
    else:
        return r * (c / w) + w


# with open('r1c_a.in') as f:
with open('A-small-attempt3.in') as f:
    with open('r1c_a_3.out', 'w') as fo:
        lines = f.readlines()
        t = int(lines[0].strip())
        for k in range(t):
            x1, x2, x3 = map(int, lines[k + 1].strip().split())

            res = solve(x1, x2, x3)
            print 80*'#'
            print res
            print 'Case #%s: %s\n' % (k + 1, res)
            fo.write('Case #%s: %s\n' % (k + 1, res))