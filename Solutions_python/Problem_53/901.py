#!/usr/bin/env python

"""Google Code Jam 2010, Qualification round."""

import sys

def read_from(fh, num):
    return [fh.readline() for i in xrange(num)]

def calc_res(n, k):
    if k == 0 or k < n:
        return "OFF"
    else:
        #must calculate.  Note that the switch in position i (from the left)
        #will toggle every 2^(i-1) steps.
        x = k + 1
        for i in range(n):
            x = x / 2.
            if x - int(x) > 0:
                return "OFF"
        return "ON"





        
def main(args):
    if len(args) < 2:
        return 1
    try:
        f = open(args[1])
        #READ appropriate args from initial lines
        T = int(f.readline())
        for case in xrange(T):
            #READ appropriate args for this case
            N, K = [int(x) for x in f.readline().split()]
            #CALCULATE answer for this case
            print "Case #" + str(case+1) + ": " + str(calc_res(N, K))
    except IOError:
        print "Invalid file input"
        return 2

if __name__ == '__main__':
    sys.exit(main(sys.argv))
