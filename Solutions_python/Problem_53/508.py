# -*- coding: utf-8 -*-

t = int(raw_input())
for x in xrange(1, t + 1):
    n, k = [int(i) for i in raw_input().split(' ')]
    stateon = 2 ** n
    
    if ((k + 1) % stateon) == 0:
        print 'Case #%d: ON' % x
    else:
        print 'Case #%d: OFF' % x
