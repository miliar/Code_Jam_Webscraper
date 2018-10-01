# -*- coding: utf-8 -*-

t = int(raw_input())

for x in xrange(1, t + 1):
    r, k, n = [int(c) for c in raw_input().split(' ')]
    g = [int(c) for c in raw_input().split(' ')]
    money = 0
    i = 0
    
    while r > 0:
        j = 0
        places = 0
        
        while places < k and j < n:
            newplaces = places + g[i]
            if newplaces > k:
                break
            places = newplaces
            i += 1
            j += 1
            if i >= n:
                i = 0
        
        money += places
        r -= 1
    
    print 'Case #%d: %d' % (x, money)
