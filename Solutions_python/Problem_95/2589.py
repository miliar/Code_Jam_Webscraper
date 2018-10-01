#!/usr/bin/env python

from string import maketrans
import sys

mapin  = "ynficwlbkuomxsevzpdrjgthaq"
mapout = "abcdefghijklmnopqrstuvwxyz"
translation = maketrans(mapin, mapout)

def next_case(file_name):
    """A generator that returns the next case to be reversed"""

    f = open(file_name, 'r')
    num_of_cases = int(f.readline())

    for i in xrange(num_of_cases):
        yield f.readline()

if __name__ == '__main__':
    i = 1
    for sentence in next_case(sys.argv[1]):
        print "Case #" + str(i) + ':',
        print sentence.translate(translation),
        i += 1
