#!/usr/bin/env python
"""
bot.py: Bot Trust

Google Code Jam
Qualification Round 2011
Problem A: Bot trust


Author: Kelsey Jordahl <kajord@gmail.com>
Time-stamp: <Sat May  7 14:00:07 EDT 2011>

"""

import sys
from numpy import array

verbose = True
debug = False

def time(N, R, P):
    """
    Find the time for the two robots ('O' and 'B') to push all the buttons in order
    Solve by simulation
    """
    posO = 1
    posB = 1
    t = 0
    if verbose:
        print '%5s | %18s | %18s' % ('Time','Orange','Blue')
        print '------+--------------------+-------------------'
    while P:
        t += 1
        actO = 'Stay at button %d' % posO           # Default action
        actB = 'Stay at button %d' % posB           # in case there's nothing to do
        try:
            nextO = P[R.index('O')]
        except ValueError:
            nextO = None
        try:
            nextB = P[R.index('B')]
        except ValueError:
            nextB = None
        # print 'O goal %s, B goal %s' % (str(nextO), str(nextB))
        if nextO is not None:
            if posO == nextO:           # at the right place
                if R[0]=='O':
                    actO = 'Push button %d' % posO
                    P.pop(0) 
                    R.pop(0)
                else:
                    actO = 'Stay at button %d' % posO
            elif posO < nextO:
                posO += 1
                actO = 'Move to button %d' % posO
            elif posO > nextO:
                posO -= 1
                actO = 'Move to button %d' % posO
        if nextB is not None:
            if posB == nextB:           # at the right place
                if R[0]=='B' and actO[:4] != 'Push': # can't push both!
                    actB = 'Push button %d' % posB
                    P.pop(0) 
                    R.pop(0)
                else:
                    actB = 'Stay at button %d' % posB
            elif posB < nextB:
                posB += 1
                actB = 'Move to button %d' % posB
            elif posB > nextB:
                posB -= 1
                actB = 'Move to button %d' % posB
        if verbose:
            print '%5d | %18s | %18s' % (t, actO, actB)
    return t

def main():
    if len(sys.argv) < 2:
        infile = 'bottest.in'
    else:
        infile = sys.argv[1]
    if len(sys.argv) < 3:
        outfile = infile + '.out'
    else:
        outfile = sys.argv[2]
    if verbose:
        print 'infile %s, outfile %s' % (infile, outfile)
    f = open(infile)
    o = open(outfile,'w')
    T = int(f.readline())
    print 'T = %d' % T
    for i in range(0,T):
        a = f.readline().split()
        N = int(a[0])
        a.pop(0)
        R = a[::2]
        P = [int(c) for c in array(a[1::2])]
        print 'Case #%d' % (i+1)
        if debug:
            print R
            print P
        o.write('Case #%d: %d\n' % (i+1, time(N, R, P)))
    f.close
    o.close

if __name__ == '__main__':
    main()
