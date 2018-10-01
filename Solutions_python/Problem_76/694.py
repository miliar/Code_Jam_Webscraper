#!/usr/bin/env python
"""
candy.py: Sean and Patrick splitting candy

Google Code Jam
Qualification Round 2011
Problem C: Candy splitting


Author: Kelsey Jordahl <kajord@gmail.com>
Time-stamp: <Sat May  7 11:16:37 EDT 2011>

"""

import sys
from numpy import array

verbose = True
debug = False

def xor(l):
    """
    Bitwise XOR of elements of a list
    (this is how Sean adds)
    """
    s = l[0]
    for i in range(1,len(l)):
        s = s ^ l[i]
    return s


def haul(l):
    """
    Calculate Sean's maximum haul for a list l
    """
    N = len(l)
    haul = None
    # to do this exhaustively is O(2**N)
    for i in range(1,2**N-1):
        st = bin(i)
        idx = [int(c) for c in st[2:]]   # list of (0,1) values for digits
        while len(idx)<N:               # bring up to length N
            idx = [0] + idx
        idx = array(idx) == 1           # convert to true boolean array
        sean = l[idx]
        patrick = l[~idx]
        if debug:
            print 'Sean %s, Patrick %s' % (sean, patrick)
        if xor(sean) == xor(patrick):   # Patrick thinks they're equal
            s = sum(sean)
            if debug:
                print 'Sean has %d' % s
            if s>haul:
                haul = s
    return haul

def main():
    if len(sys.argv) < 2:
        infile = 'test.in'
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
        N = int(f.readline())
        line = f.readline()
        l = array([int(c) for c in line.split()])
        print 'Case #%d: N = %d' % (i+1, N)
        h = haul(l)
        if verbose:
            print 'Haul: %s' % str(h)
        if h:
            o.write('Case #%d: %d\n' % (i+1, h))
        else:
            o.write('Case #%d: NO\n' % (i+1))
    f.close
    o.close

if __name__ == '__main__':
    main()
