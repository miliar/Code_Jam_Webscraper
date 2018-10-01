#!/usr/bin/python

import itertools
from fractions import gcd


c = int(raw_input())

for i in xrange(c):
    t = map(lambda x : int(x), raw_input().strip('\n').split()[1:])
    d = reduce(lambda x,y : gcd(x, y), (abs(x - t[0])  for x in t[1:]), 0)
    y = min( (((x - 1) / d + 1) * d - x) for x in t)
    print 'Case #%d: %d'  %(i + 1, y) 



        
        
    



