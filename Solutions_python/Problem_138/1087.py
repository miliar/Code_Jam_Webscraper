#!/usr/bin/env python

import sys
import bisect

eps = 0.0000001

def getWar(N, Naomi, Ken):
    points = 0
    for n in Naomi:
        if n > Ken[-1]:
            points += 1
            Ken.pop(0)
        else:
            k = Ken.pop(bisect.bisect(Ken, n))
            if k < n:
                points += 1
            #endif
        #endif
    #endfor
    return points
#enddef

def getDWar(N, Naomi, Ken):
    points = 0
    i = 0
    while True:
        if not Ken:
            break
        #endif
        
        if Naomi[-1] > Ken[-1]:
            points += 1
            Naomi.pop(-1)
            Ken.pop(-1)
            continue
        else:
            n = Naomi.pop(0)
            k = Ken.pop(-1)
        #endif
    #endwhile
    return points
#enddef

def solve():
    N = int(sys.stdin.readline())
    Naomi = sorted(float(one) for one in sys.stdin.readline().split(" "))
    Ken = sorted((float(one) for one in sys.stdin.readline().split(" ")))
    
    return "%d %d" % (getDWar(N, Naomi[:], Ken[:]), getWar(N, Naomi, Ken))
#enddef

def main():
	T = int(sys.stdin.readline())
	for caseNumber in xrange(1, T+1):
	    print "Case #%d: %s" % (caseNumber, solve())
	#endfor
#enddef

if __name__ == '__main__':
	main()
#endif


