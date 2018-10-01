#!/usr/bin/python

from optparse import OptionParser
import operator

def parseOptions():
    parser = OptionParser()
    parser.add_option('-i', '--input', dest = 'input', help = 'Input file', default = 'C-small-practice.in')
    # parser.add_option('-o', '--output', dest = 'output', help = 'Output file', default = 'output.txt')
    (options, args) = parser.parse_args()
    return options

def readParameters(options):
    input = open(options.input)
    n = int(input.readline().strip())
    numCandies, values = [], []
    for i in xrange(n):
        numCandies.append(input.readline().strip())
        values.append([int(x) for x in input.readline().strip().split()])
    return n, numCandies, values

def findMaxBag(numCandies, values):
    totalXor = 0
    for v in values:
        totalXor ^= v
    if totalXor != 0:
        return 'NO'
    maxPile = sum(values) - min(values)
    return str(maxPile)

def main(options):
    n, numCandies, values = readParameters(options)
    results = []
    for i in xrange(n):
        result = findMaxBag(numCandies[i], values[i])
        results.append('Case #%d: %s' % (i+1, result))
    open(options.input.replace('.in', '.out'), 'w').write('\n'.join(results))
    for r in results:
        print r

if __name__ == "__main__":
    options = parseOptions()
    main(options)
