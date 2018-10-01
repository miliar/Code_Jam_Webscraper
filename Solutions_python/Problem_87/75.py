#!/usr/bin/env python
import sys
#import math

current = sys.argv[1].split('.')[0]

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

def st(s, r, t, seg):
    nseg = {}
    ret = 0
    for i in sorted(seg.keys()):
        if t:
            tempt = seg[i] / (i + float(r))
            if tempt > t:
                ret += t
                seg[i] -= t * (i + r)
                t = 0
            else:
                ret += tempt
                t -= tempt
                seg[i] = 0
        ret += seg[i] / (i + float(s))
    return ret

case = int(lines[0])
cur = 1
for i in range(1, case + 1):
    x, s, r, t, n = [int(j) for j in lines[cur].split()]
    seg = {}
    for k in range(1, n+1):
        b, e, w = [int(l) for l in lines[cur+k].split()]
        if w in seg:
            seg[w] += e - b
        else:
            seg[w] = e - b
    seg[0] = x - sum(seg.values())
    cur += 1 + n
    #print 'Case #%d: %s' % (i, st(s, r, t, seg))
    g.write('Case #%d: %s\n' % (i, st(s, r, t, seg)))

g.close()
