import sys
import psyco
psyco.full()

FILE = 'A-small-attempt0.in'
#FILE = 'input.txt'
f = open(FILE, 'r')
sys.stdout = open(FILE + '.out', 'w')

def rs():
    return f.readline()[:-1]

def ri():
    return int(f.readline())

def ra():
    return [int(s) for s in rs().split()]


ncases = int(f.readline())

for ncase in xrange(1, ncases+1):
    n, a, b, c, d, x0, y0, m = ra()
    x = x0
    y = y0
    ps = []
    ps.append((x, y))
    for i in xrange(1,n):
        x = (a * x + b) % m
        y = (c * y + d) % m
        ps.append((x, y))
    
    c = 0
    for i in xrange(n):
        for j in xrange(i+1, n):
            for k in xrange(j+1, n):
                if (ps[i][0] + ps[j][0] + ps[k][0]) % 3 == 0:
                    if (ps[i][1] + ps[j][1] + ps[k][1]) % 3 == 0:
                        c += 1
        
    print 'Case #%d: %d' % (ncase, c)
