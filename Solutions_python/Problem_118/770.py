#!/usr/bin/env python

import sys
import math

def check_region(nd, rmin, rmax): #end exclusive
    n = 0
    (nd1,nd2) = (nd//2, nd % 2)
    def check_num(num):
        if (num >= rmin and num < rmax):
            sq = str(num ** 2)
            if (sq == sq[::-1]):
                return True
        return False
    start = int(math.floor(rmin / 10 ** (nd - nd1)))
    end = int(math.ceil(rmax / 10 ** (nd - nd1)))
    for i in xrange(start, end+1):
        istr = str(i) if i > 0 else str()
        if (nd2):
            for j in xrange(0,10):
                num = istr + str(j) + istr[::-1]
                n += check_num(int(num))
        else:
            n += check_num(int(istr + istr[::-1]))
    return n



def main():
    count = int(sys.stdin.readline().rstrip())
    for case in xrange(1, count+1):
        sys.stderr.write("%d\n" % case)
        line = sys.stdin.readline().rstrip()
        (nmin, nmax) = map(int, line.split())
        rmin = int(math.ceil(math.sqrt(nmin)))
        rmax = int(math.floor(math.sqrt(nmax)))
        rmin_l = len(str(rmin))
        rmax_l = len(str(rmax))
        n = 0;
        if (rmin_l < rmax_l) :
            for nd in range(rmin_l+1,rmax_l):
                n += check_region(nd, 10** (nd-1), 10 ** nd)
            n += check_region(rmin_l, rmin, 10**rmin_l)
            n += check_region(rmax_l, 10**(rmax_l-1), rmax+1)
        else: # rmin_l == rmax_l
            n = check_region(rmin_l, rmin, rmax+1)
        print "Case #%d: %d" % (case,n);

main()



