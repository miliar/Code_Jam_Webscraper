#!/usr/bin/env 
import sys
import time
from pprint import pprint
# Case #1: 1.0000000
# Case #2: 39.1666667
# Case #3: 63.9680013
# Case #4: 526.1904762

def do_case(f):
    C, F, X = map(float, f.readline().split())
    rate = 2.0
    et = 0.0
    cookies = 0
    while (X/(rate + F) + C/rate) < X/rate:
        if C/rate == X:
            return time + C/rate
        et += (C/rate)
        rate += F
    return et+ X/rate

def main():
    f = open(sys.argv[1])
    T = int(f.readline())
    for t in xrange(1,T+1):
        print 'Case #{}: {}'.format(t, do_case(f))
    f.close()

if __name__ == '__main__':
    main()    
