#! /usr/bin/env python

import math
import itertools

#  +---+---+---+
#  | a | b | c |
#  +---+---+---+
#  0   1   2   3
# -3  -2  -1

def split(P,k):
    
    M = max(P)
    time = k + M
    if ( all([x == 1 for x in P]) ):
        return time
    else:
        k += P.count(M)
        # print('k',k)
        
        m = int(math.floor(M/2))
        for i in range(1,m+1): 
            # print('i',i)
            temp = list(map(lambda x: [i,x - i] if x == M else [x], P))
            newP = list(itertools.chain.from_iterable(temp))
            # print('P',P)
            # print('time',k + max(newP))
            newtime = split(newP,k)
            if newtime < time:
                time = newtime
                minutes = k
        return time
        
if __name__ == "__main__":
    T = int( input() )
    
    for x in range(1,T+1):
        
        D = int( input() )
        
        P = list(map(int,input().split()))
        
        M = max(P)
        time = M
        for m in range(1,M):
            # print('m',m)
            time = min(time,sum([(x-1) // m for x in P]) + m)
        # print('Case #%i: %i' % (x,time))
        
        # time = split(P,0)
        print('Case #%i: %i' % (x,time))
