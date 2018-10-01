#!/usr/bin/env python

import os, sys
import codejam

def candysplitting(testcase):
    # The key takeaway here is that Patrick is XORing the values.
    # Further, if there is a group with equal XOR to the other group, then XORing those together makes zero.
    # Which means that the XOR of the whole thing is zero if and only if there is an equal XOR.
    # And indeed, at that point we can just pick out the smallest piece of candy and hand it to Patrick
    # and we can keep all the rest.
    if len(testcase) != 2:
        raise RuntimeError, "Oops, we got a bad testcase!"
    numvals = int(testcase[0])
    vals = [int(x) for x in testcase[1].split(" ")]
    if len(vals) != numvals:
        raise RuntimeError, "Oops, we got %d values when we were told %d" % (len(vals), numvals)
    smallestval = 9999999
    sumofvals = 0
    xorofvals = 0
    for i in vals:
        if i < smallestval:
            smallestval = i
        xorofvals ^= i
        sumofvals += i

    if xorofvals != 0:
        return "NO"
    else:
        return "%d" % (sumofvals - smallestval)

if __name__ == "__main__":
    codejam.main(sys.argv[1:], candysplitting, 2)
