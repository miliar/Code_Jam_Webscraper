#!/usr/bin/python

import sys
from math import sqrt

cache = {}

def is_possible(vines, cur_vine, cur_height, D, indent):
    global cache
    #print "cur",indent, cur_vine, cur_height
    cur_d = vines[cur_vine][0]

    if cur_d + cur_height >= D:
        return True
    if cur_vine in cache and cache[cur_vine] >= cur_height:
        #print 'cache hit'
        return False

    for vin in range(cur_vine+1, len(vines)):
        if cur_vine in cache and cache[cur_vine] >= cur_height:
            #print 'cache hit'
            return False
        vin_d, vin_height = vines[vin]
        #print "vin", vin_d, vin_height
        if vin_d > cur_d + cur_height:
            #store in cache
            #print "cached", cur_vine, cur_height
            if cur_vine in cache:
                cache[cur_vine] = max(cur_height, cache[cur_vine])
            else:
                cache[cur_vine] = cur_height
            return False
        max_ht = sqrt(cur_height**2 - (vin_d - cur_d)**2)
        vin_poss = min(max_ht, vin_height)
        vin_poss = max(vin_poss, vin_d - cur_d)
        vin_poss = min(vin_height, vin_poss)
        #print vin_poss
        #print ">"
        if is_possible(vines, vin, vin_poss, D, indent+1):
            return True

    #print "cached", cur_vine, cur_height
    if cur_vine in cache:
        cache[cur_vine] = max(cur_height, cache[cur_vine])
    else:
        cache[cur_vine] = cur_height
    return False


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for i in range(1, T+1):
        N = int(sys.stdin.readline().strip())
        vines = []
        for j in range(N):
            d, l = tuple([int(k) for k in sys.stdin.readline().split()])
            vines.append((d,l))

        D = int(sys.stdin.readline().strip())
        d0, l0 = vines[0]

        cache.clear()
        if (is_possible(vines, 0, d0, D, 0)):
            print 'Case #{0}: YES'.format(i)
        else:
            print 'Case #{0}: NO'.format(i)
