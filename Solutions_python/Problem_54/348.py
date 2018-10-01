#!/usr/bin/env python

p = 'B'
s = 'small-attempt%d' % 0
l = 'large'
current = '%s-%s' % (p, l)

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

def gcd(a, b):
    if b:
        return gcd(b, a % b)
    else:
        return a

def listgcd(n, l):
    d = abs(l[1] - l[0])
    for i in range(2, n):
        d = gcd(d, abs(l[i] - l[i - 1]))
    return d

case = int(lines[0])
for i in range(1, case + 1):
    l = lines[i].split(' ')
    n = int(l.pop(0))
    l = [int(x) for x in l]
    d = listgcd(n, l)
    t = d - l[0] % d if l[0] % d else 0
    #print 'Case #%d: %d\n' % (i, t)
    g.write('Case #%d: %d\n' % (i, t))

g.close()
