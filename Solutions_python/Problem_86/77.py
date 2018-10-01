#!/usr/bin/env python
import sys
import math

current = sys.argv[1].split('.')[0]

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

def gcd(x, y):
    if y > x:
        x, y = y, x
    while x and y:
        x, y = y, x % y
    return x

def lgcd(l):
    if len(l) < 2:
        return l[0]
    ret = gcd(l[0], l[1])
    for i in range(2, len(l)):
        ret = gcd(ret, l[i])
    return ret

def note(n, l, h, others):
    for i in range(l, h+1):
        temp = 0
        for j in others:
            if temp:
                break
            if j < i:
                temp += i%j
            else:
                temp += j%i
        if not temp:
            return i
    return 'NO'
    '''gd = lgcd(others)
    if gd >= l and gd <= h:
        return gd
    gd = others[0]
    p = 1
    for i in range(n):
        gd = gcd(gd, others[i])
        p *= others[i]
        lm = p / gd
        if lm > h:
            break
        if lm < l:
            continue
        if all([x % lm == 0 for x in others[i+1:]]):
            return lm
    return 'NO''''

case = int(lines[0])
for i in range(1, case + 1):
    l = lines[2 * i - 1].split()
    n, l, h = [int(x) for x in l]
    others = lines[2 * i].split()
    others = [int(x) for x in others][:n]
    others.sort()
    #print 'Case #%d: %s' % (i, note(n, l, h, others))
    g.write('Case #%d: %s\n' % (i, note(n, l, h, others)))

g.close()
