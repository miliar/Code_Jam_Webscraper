# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(1000000)
rl = lambda: sys.stdin.readline().strip()


def fit(org, made):
    if len(made) == len(org):
        return made
    pos = len(made)
    for x in map(str, range(10))[::-1]:
        if x == '0' and pos == 0:
            continue
        if int(''.join(org[:pos + 1])) < int(''.join(made + [x])):
            continue
        if pos != 0 and made[pos - 1] > x:
            continue
        ret = fit(org, made + [x])
        if ret:
            return ret


T = int(rl())
for tcase in range(1, T + 1):
    x = rl()
    print >> sys.stderr, tcase, x
    if len(x) == 1:
        print 'Case #%d: %s' % (tcase, x)
        continue
    org = [_x for _x in x]
    ret = fit(org, [])
    if ret:
        print 'Case #%d: %s' % (tcase, ''.join(ret))
    else:
        print 'Case #%d: %s' % (tcase, ''.join(['9' for i in range(len(org) - 1)]))
