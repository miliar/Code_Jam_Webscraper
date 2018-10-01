import sys
import fileinput
from fractions import gcd

i=0
for line in fileinput.input():
    if i>0:
        t = line.split(' ')
        t = t[1:]
        t = [int(x) for x in t]
        m = min(t)
        t = [x-m for x in t]
        g=0
        for x in t:
            g=gcd(g,x)
        print 'Case #%d: %d' % (i, (-m)%g)
    i+=1



