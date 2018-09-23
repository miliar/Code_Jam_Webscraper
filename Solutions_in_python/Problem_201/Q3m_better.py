from heapq import *
import math

def helper():
    input = raw_input()
    S, K = map(int, input.strip().split())

    if S <= K:
        return 0,0    
    else:
        heap = [] 
        
        heappush(heap, -S)
        for i in range(K - 1):
            empty = - heappop(heap) - 1
            left = empty / 2
            right = empty - left
            heappush(heap, - left)
            heappush(heap, - right)

        empty = - heappop(heap) - 1
        a = empty / 2
        b = empty - a

        return max(a, b), min(a, b)       

        

for case in xrange(input()):
    a, b = helper()
    print 'Case #%d: %s %s' % (case+1, a, b)