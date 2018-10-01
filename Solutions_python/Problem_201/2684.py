import numpy as np
import math


def initialize_stalls(N):
    stalls = [0]*(N+2)

    # fill w. bathroom guards
    stalls[0] = 1
    stalls[len(stalls) - 1] = 1
    return stalls

def largest_gap(stalls):
    occupied = np.nonzero(stalls)[0]
    gap = -1 # gap is magnitude of difference in occupied stalls)
    for i in xrange(len(occupied)-1,0,-1):
        current_occ_stall = occupied[i]
        next_occ_stall = occupied[i-1]
        new_gap = current_occ_stall-next_occ_stall
        if new_gap >= gap:
            gap = new_gap
            stall_location = next_occ_stall + (int(math.ceil(new_gap/2)))
            ls = stall_location - next_occ_stall - 1
            rs = current_occ_stall - stall_location - 1

    # print "new_gap: {}".format(new_gap)
    # print "stall_location: {}".format(stall_location)

    return stall_location, ls, rs

def populate_next_stall(stalls):
    index,ls,rs = largest_gap(stalls)
    stalls[index] = 1
    return stalls,ls,rs

def loop(stalls,K):
    while K > 0:

        stalls,ls,rs = populate_next_stall(stalls)
        # print stalls
        K-=1
    lastls = ls
    lastrs = rs

    return max(lastls,lastrs),min(lastls,lastrs)

t = int(raw_input())
for i in xrange(1,t+1):
    n = [int(s) for s in raw_input().split(" ")]

    stalls = initialize_stalls(n[0])
    maximum,minimum = loop(stalls,int(n[1]))

    # print "NEXT CASE"

    print "Case #{}: {} {}".format(i,maximum,minimum)
