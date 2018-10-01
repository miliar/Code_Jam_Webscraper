from optparse import OptionParser
import string
import math
import re


def solve(name, N):
    substrings = 0
    first = 0
    size = len(name)
    exp = re.compile("^[bcdfghjklmnpqrstvwxyz]{%s}" % N)
    for i in xrange(size + 1 - N):
        if exp.match(name[i:]):
            new_starts = (i + 1) - first
            ends = size - (i + N - 1)
            substrings += new_starts * ends
            #for j in xrange(first, i+1):
            #    for k in xrange(i+N-1, size):
            #        substrings.add((j,k))
            first = i+1
    return substrings

def main():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="read input from FILE", metavar="FILE")

    (options, args) = parser.parse_args()
    if not options.filename:
        parser.error("Must provide a filename.")
    input_file = open(options.filename, "r")
    total_cases = int(input_file.readline())
    case_number = 0
    while case_number < total_cases:
        case_number += 1
        bits = input_file.readline().split(' ')
        name = bits[0]
        N = int(bits[1])
        print "Case #%d: %s" % (case_number, solve(name, N))

if __name__ == "__main__":
    main()