#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools, collections
import sys
import math
import fractions
import string

def input_read(filename):
    data = None
    with open(filename) as f:
        for x in f:
            yield [int(s.strip()) for s in x.split()]

def output_file(filename, ans):
    with open(filename, 'w') as f:
        for n, a in enumerate(ans,1):
            f.write('Case #%d: %d\n' % (n, a))
    return

def gen_testcase(ifilename):
    itr = input_read(ifilename)
    [T] = next(itr)
    for x in range(T):
        yield next(itr)

def solve_one(r, t):
    print("r, t = %d, %d" % (r, t) )
    b = ( 2 * r - 1)
    x = ( - b + math.sqrt( pow(b,2) + 8 * t)) / 4
    print ("x = %s" % x)
    k = math.floor(x)
    assert(k >= 0)
    return k 

def solve_all(inputfile):
    for r, t in gen_testcase(inputfile):
         yield solve_one(r, t)

def main(ifile, ofile):
    output_file(ofile, solve_all(ifile))
    return

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    #parser.add_option('-i', type='string', dest='ifile', help='input filename', default='input.txt')
    parser.add_option('-o', type='string', dest='ofile', help='output filename', default='output.txt')
    
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.print_help()
        sys.exit()

    try:
        main(args[0], options.ofile)
    except IOError as data:
        print(data)

