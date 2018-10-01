#!/usr/bin/env python
# -*- coding: latin-1 -*-
def test_snapper(n, k):
    snapper_mask = (1 << n) - 1
    all_snappers = k #the snappers follow binary rules, just  counter
    return ( ((~all_snappers)&snapper_mask) == 0 )
if __name__ == "__main__":
    import sys
    infile = "A-large.in"
    case_number = 1
    myfile = open(infile)
    number_test = int(myfile.readline())
    case_number = 1
    while number_test:
        line = myfile.readline()
        N,K = map(int, line.split())
        print "Case #%d:" % case_number,
        if test_snapper(N,K):
            print "ON"
        else:
            print "OFF"
        number_test -= 1
        case_number += 1

