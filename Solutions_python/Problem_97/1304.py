#!/usr/bin/env python
import sys

current = sys.argv[1].split('.')[0]

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

def recycle(n, b):
    l, ret, tmp = len(str(n)), set(), n
    for i in range(l):
        tmp = tmp % 10 * 10 ** (l - 1) + tmp / 10
        if tmp > n and tmp <= b:
            ret.add(tmp)
    return ret

def prep():
    ret = []
    for i in range(0, 2000000):
        possible = recycle(i, 2000000)
        ret.append(possible)
    return ret        

def count(a, b, preped):
    ret = 0
    for i in range(a, b):
        possible = [x for x in preped[i] if x <= b]
        ret += len(possible)
    return ret

preped = prep()
case = int(lines[0])
for i in range(1, case + 1):
    l = lines[i].split(' ')
    a, b = [int(x) for x in l]
    g.write('Case #%d: %d\n' % (i, count(a, b, preped)))

g.close()
