#!/usr/bin/python

import operator, math, re, os, sys
from optparse import OptionParser

def parseOptions():
    parser = OptionParser()
    parser.add_option('-i', '--input', dest = 'input', help = 'Input file', default = 'C-small-attempt1.in')
    # parser.add_option('-o', '--output', dest = 'output', help = 'Output file', default = 'output.txt')
    (options, args) = parser.parse_args()
    return options

def readParameters(options):
    input = open(options.input)
    n = int(input.readline().strip())
    number, low, high, freqs = [], [], [], []
    for i in xrange(n):
        vals = input.readline().strip().split()
        number.append(int(vals[0]))
        low.append(int(vals[1]))
        high.append(int(vals[2]))
        tmp = input.readline().strip().split()
        freqs.append([int(x) for x in tmp])
    return n, number, low, high, freqs

def findFreq(number, low, high, freqs):
    for f in xrange(low, high+1):
        good = True
        for freq in freqs:
            if f > freq:
                if f % freq != 0:
                    good = False
                    break
            if freq > f:
                if freq % f != 0:
                    good = False
                    break
        if good:
            return str(f)
    return 'NO'

def main(options):
    n, number, low, high, freqs = readParameters(options)
    results = []
    for i in xrange(n):
        result = findFreq(number[i], low[i], high[i], freqs[i])
        print number[i], low[i], high[i], result
        results.append('Case #%d: %s' % (i+1, result))
    open(options.input.replace('.in', '.out'), 'w').write('\n'.join(results))
    for r in results:
        print r

if __name__ == "__main__":
    options = parseOptions()
    main(options)
