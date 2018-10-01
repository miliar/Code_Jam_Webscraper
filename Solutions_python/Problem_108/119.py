#! /usr/bin/python
# -*- coding: utf8 -*-

from heapq import heappush, heappop


def reach(status,vines):
    radius = min(vines[status[1]][0] - status[0], vines[status[1]][1])
#    print 'R', status, vines[status[1]], vines[status[1]][0], radius, vines[status[1]][0]+radius
    return vines[status[1]][0]+radius

def do_calc(d,vines):
#    print d,vines
    hq = []
    heappush(hq, [0,0])

    while hq:
        status = heappop(hq)
        r = reach(status,vines)
        if ( r >= d ):
            return True
        for i in range(status[1]+1,len(vines)):
            if ( r >= vines[i][0] ):
                heappush(hq,[vines[status[1]][0],i])

    return False

def main():
    for c in range(input()):
        vines = []
        for v in range(input()):
            vines.append(map(int,raw_input().split()))
        d = input()
        ans = do_calc(d,vines) 
        print 'Case #%d: %s' % (c+1, 'YES' if ans else 'NO' )

if __name__ == '__main__':
    main()
