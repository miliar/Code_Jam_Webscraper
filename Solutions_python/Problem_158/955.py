#!/usr/bin/env python
import sys
import ipdb

def calc(x, r, c):
    if r > c:
        r,c = c,r
    #e now r is smaller
    #
    # 1.
    if x == 1:
        return 'GABRIEL'
    if x > c:
        return 'RICHARD'

    # 2.
    if (r*c)%x != 0:
        return 'RICHARD'

    if x >= 7:
        return 'RICHARD'

    if x >= (2*r):
        if x == 2:
            return 'GABRIEL'
        if r > 1 or c > 2:
            return 'RICHARD'

    # thats it

    return 'GABRIEL'

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ifile = open(sys.argv[1])
    else:
        ifile = sys.stdin
    if len(sys.argv) > 2:
        ofile = open(sys.argv[2])
    else:
        ofile = sys.stdout
    testcases = int(ifile.readline())

    for i in range(testcases):
        x, r, c = [int(v) for v in ifile.readline().split(' ')]
        print "Case #%i: %s" % (i+1, str(calc(x,r,c)))
