#!/usr/bin/env python

import sys, os, re
#from collections import deque

#---------------------------------------------------
# Function 
#---------------------------------------------------
def osmos(mote, mlist):
    mlist.sort()

    poss = [] 
    poss.append([0, mote, 0])   # operation, mote, index
    total = len(mlist)

    while len(poss) > 0:
        poss.sort()
        ope, sz, idx = poss[0]
        del poss[0]
        assert idx <= total
        if idx == total: return ope 
        dst = mlist[idx]
        if dst < sz:
            poss.append([ope, sz+dst, idx+1])
        else:
            poss.append([ope+1, sz, idx+1])
            poss.append([ope+1, sz+sz-1, idx])
    return total

def load_file(filename):
    with open(filename, 'rU') as f:
        number = int(f.readline())
        for i in range(number):
            m, N = [int(v) for v in f.readline().split()][0:2]
            mlist = [int(v) for v in f.readline().split()][0:N]
            result = osmos(m, mlist) 
            print 'Case #%d: %s' % (i+1, result)
    return

#---------------------------------------------------
# Entry Point 
#---------------------------------------------------
def main():
    #if len(sys.argv) < 3:
    #    print 'Usage:'
    #    print '  %s arg1 arg2' % os.path.basename(sys.argv[0])
    #    sys.exit(1)

    load_file (sys.argv[1])

    return

#---------------------------------------------------
# Unit Test Entry 
#---------------------------------------------------
if __name__ == '__main__':
    main()


