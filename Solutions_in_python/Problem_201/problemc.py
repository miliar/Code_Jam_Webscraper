# Problem C Bathroom Stalls
import heapq
import collections
import time

class MaxPriorityQueue:
    def __init__(self):
        self.h = []
        self.counts = collections.Counter()
    def push(self, v, count):
        if not v in self.counts:
            heapq.heappush(self.h, -v)
        self.counts[v] += count
    def pop(self):
        top = -heapq.heappop(self.h)
        return (top, self.counts[top])
            

n = int(raw_input())
for i in xrange(1,n+1):
    
    n, k = [int(s) for s in raw_input().split(" ")]

    regions = MaxPriorityQueue()
    regions.push(n, 1)

    hs = 1

    p = 1
    while p < k+1:
        r,rcount = regions.pop()

        if r % 2 == 0:
            # Pick middle left
            s = r / 2
        else:
            # Pick middle
            s = (r / 2) + 1

        #print "Person {} selected stall {}".format(p,s)

        LS = s - 1
        RS = r - s

        #print "s: {} LS: {} RS: {}".format(s,LS,RS)
        
        regions.push(LS,rcount)
        regions.push(RS,rcount)

        p += rcount

        if len(regions.h) > hs:
            hs = len(regions.h)
    
    print "Case #{}: {} {}".format(i,max(LS,RS),min(LS,RS))
