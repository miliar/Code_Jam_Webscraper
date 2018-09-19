import sys
from numpy import *

inf = open('A.in','r')

T = [int(x) for x in inf.readline().split()][0]

for t_case in range(1,T+1):
    num_full = [int(x) for x in inf.readline().split()][0]
    cakes = [int(x) for x in inf.readline().split()]
    
    
    cakes.sort()
    cakes.reverse()
    dp_dict = {}
    def recurse(prev_plate_size, secs_used, idx):
        if idx >= num_full:
            return secs_used + prev_plate_size
        
        key = (idx, prev_plate_size, secs_used)
        
        if key in dp_dict:
            return dp_dict[key]
        
        best = max(cakes[idx],prev_plate_size) + secs_used
        cur_plate = cakes[idx]
    
        for split in range(2, int(ceil(sqrt(cur_plate))) + 1):
            max_size = max( ceil(1.0*cur_plate/split), prev_plate_size)
            next = recurse(max_size, secs_used+split-1, idx+1)
            if next < best:
                best = next
        
        dp_dict[key] = best
	return best
    
    best = recurse(0,0,0)
    print 'Case #%d: %d' % (t_case, best)
