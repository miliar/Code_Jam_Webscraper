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
    seqLengths, sequences = [], []
    for i in xrange(n):
        vals = input.readline().strip().split()
        seqLengths.append(int(vals[0]))
        sequence = []
        for j in xrange(seqLengths[i]):
            sequence.append([vals[1+j*2], int(vals[2+j*2])])
        sequences.append(sequence)
    return n, seqLengths, sequences

def findMinTime(seqLengths, sequence):
    oTime, bTime = 0, 0
    oLastPlace, bLastPlace = 1, 1
    # print sequence
    for step in sequence:
        # print step, oTime, bTime, ' ==>', 
        newPlace = step[1]
        if step[0] == 'O':
            distance = abs(newPlace - oLastPlace)
            oTime = max([oTime+ distance, bTime]) + 1
            oLastPlace = newPlace
        else:
            distance = abs(newPlace - bLastPlace)
            bTime = max([bTime+ distance, oTime]) + 1
            bLastPlace = newPlace
        # print oTime, bTime
    return max(oTime, bTime)

def main(options):
    n, seqLengths, sequences = readParameters(options)
    results = []
    for i in xrange(n):
        result = findMinTime(seqLengths[i], sequences[i])
        results.append('Case #%d: %s' % (i+1, result))
    open(options.input.replace('.in', '.out'), 'w').write('\n'.join(results))
    for r in results:
        print r

if __name__ == "__main__":
    options = parseOptions()
    main(options)
