from __future__ import with_statement
from optparse import OptionParser
import sys


def process(in_file, out_file):
    num_cases = int(in_file.readline())
    for case in xrange(1, num_cases+1):
        print 'Case #%d:' % case
        result = 0
        p, k, l = [int(x) for x in in_file.readline().split(' ')]
        #print p, k, l
        frequencies = sorted([int(x) for x in in_file.readline().split(' ')])
        i, place = 0, 0
        for f in reversed(frequencies):
            if i % k == 0:
                place += 1
            result += place * f
            i += 1
        out_file.write('Case #%d: %d\n' % (case, result))


def main():
    parser = OptionParser(usage="""\
Usage: %prog [options]""")
    parser.add_option('-i', '--input_file',
            type='string', action='store')
    parser.add_option('-o', '--output_file',
            type='string', action='store')
    opts, args = parser.parse_args()
    if not opts.input_file or not opts.output_file:
        parser.print_help()
        sys.exit(1)

    with open(opts.input_file, 'r') as i:
        with open(opts.output_file, 'w') as o:
            process(i, o)


if __name__ == '__main__':
    main()

