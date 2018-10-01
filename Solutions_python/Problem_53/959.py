#! /usr/bin/env python

import sys

# N = int(sys.argv[1]) # number of snappers
# K = int(sys.argv[2]) # number of snaps

def do(N, K):
    wires = [False] * (N+1)
    wires[0] = True

    snappers = [False] * N

    # print "Initial"
    # print "snappers: %s" % snappers
    # print "wires: %s" % wires

    for _ in xrange(K):
        for i, snapper in enumerate(snappers):
            if wires[i]:
                snappers[i] = not snappers[i]
            else:
                break
            
        for i in xrange(N):
            # if the snapper is off, cut electricity to the right
            if not snappers[i]:
                for j in xrange(i+1, N+1): wires[j] = False
            # if the snapper is on AND it's wired, let it flow to the right
            elif (snappers[i] and wires[i]):
                for j in xrange(i+1, N+1): wires[j] = True
        # 
        # print
        # print "After iteration %s" % _
        # print "snappers: %s" % snappers
        # print "wires: %s" % wires
        # print "Light lit? %s" % wires[i+1]
    return wires[-1]
        
if __name__ == '__main__':
    lines = sys.stdin.readlines(); lines.reverse()
    ncases = int(lines.pop())
    
    for case_index in xrange(ncases):
        case = lines.pop()
        N, K = map(int, case.split(' '))
        
        print "Case #%d: %s" % (case_index+1, "ON" if do(N, K) else "OFF")