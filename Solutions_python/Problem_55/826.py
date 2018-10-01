#! /usr/bin/env python

import sys

def do(R, K, gs):
    # R = number of runs
    # K = number of people at a time
    # gs = groups
    
    head = 0
    G = len(gs)
    
    euros = 0
    
    for _ in xrange(R):
        capacity = 0
        
        i = 0
        for i in xrange(head, head+G):
            j = i % G
            if capacity + gs[j] <= K:
                capacity += gs[j]
            else:
                break
                
        euros += capacity
                
        head = i
        
    return euros
        
if __name__ == '__main__':
    lines = sys.stdin.readlines(); lines.reverse()
    
    ncases = int(lines.pop())
    for i in xrange(ncases):
        R, K, n = map(int, lines.pop().split())
        gs = map(int, lines.pop().split())
        
        print "Case #%d: %d" % (i+1, do(R, K, gs))