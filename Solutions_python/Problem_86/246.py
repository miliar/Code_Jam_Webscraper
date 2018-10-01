#!/usr/bin/env python
"""
Perfect harmony

Google Code Jam
2011 Round 1C
Problem C: Perfect harmony

"""

import sys
from numpy import *

verbose = True
debug = False

def note(N, L, H, P):
    '''
    find the harmony
    '''
    for f in xrange(L,H+1):
        if debug:
            print f
        for n in set(P):
            if (n % f) and (f % n):
                fac = None
                break
            fac = f
        if fac:
            return fac
    return None
                

def main():
    if len(sys.argv) < 2:
        infile = 'C-test.in'
    else:
        infile = sys.argv[1]
    if len(sys.argv) < 3:
        if infile[-3:] == '.in':
            outfile = infile[:-3] + '.out'
        else:
            outfile = infile + '.out'
    else:
        outfile = sys.argv[2]
    if verbose:
        print 'infile %s, outfile %s' % (infile, outfile)
    f = open(infile)
    o = open(outfile,'w')
    T = int(f.readline())
    print 'T = %d' % T
    for i in xrange(T):
        l = f.readline().split()
        N = int(l[0])
        L = int(l[1])
        H = int(l[2])
        l = f.readline().split()
        P = [int(c) for c in l]
        jeff = note(N, L, H, P)
        print 'Case #%d:' % (i+1)
        o.write('Case #%d: ' % (i+1))
        if jeff is None:
            print 'NO'
            o.write('NO\n')
        else:
            print jeff
            o.write('%d\n' % jeff)
    f.close
    o.close

if __name__ == '__main__':
    main()
