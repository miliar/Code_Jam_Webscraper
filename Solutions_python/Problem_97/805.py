#!/usr/bin/env python

from __future__ import print_function, division

import math
import os
import os.path
import sys


def main():
    inFile = open(sys.argv[1], "rt")
    outFile = open(sys.argv[2], "wt")

    numCases = int(inFile.readline())

    for case in xrange(1, numCases+1):
        print("*** Case {0:d} ***".format(case))

        lowNum, highNum = [int(s) for s in inFile.readline().split()]
        digits = int(math.ceil(math.log10(highNum)))
        recycled = 0

        for num in xrange(lowNum, highNum+1):
            rotSet = set()

            for rot in xrange(1, digits):
                sepFactor = 10 ** rot
                suffix = num % sepFactor
                prefix = num // sepFactor

                combFactor = 10 ** (digits-rot)
                rotNum = suffix * combFactor + prefix

                # if case < 4:
                    # print(num, rotNum, prefix, suffix, sepFactor, combFactor, digits)

                if num < rotNum <= highNum:
                    rotSet.add(rotNum)

            recycled += len(rotSet)

        outFile.write("Case #{0:d}: {1:d}\n".format(case, recycled))

    inFile.close()
    outFile.close()


if __name__ == "__main__": main()
