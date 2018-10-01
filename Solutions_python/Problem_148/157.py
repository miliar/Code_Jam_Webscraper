#!/usr/bin/python

import sys, decimal as d, collections as coll, itertools as it, fractions as f



T = int(raw_input())
tt = max(T/10, 1)

for c in xrange(T):
    print 'Case #{}:'.format(c+1),
    if c % tt == 0:
        print >>sys.stderr, 'Solving: ', (c+1)*100/T, '%'
    
    N, X = map(int, raw_input().split() )
    
    S = coll.deque( sorted(map(int, raw_input().split() )) )
    
    #print >>sys.stderr, S
    
    
    res = 0
    while S:
        res += 1
        if len(S) == 1:
            break
        
        if S[-1] + S[0] <= X:
            S.pop()
            S.popleft()
        else:
            S.pop()
    
    print res
            
    
