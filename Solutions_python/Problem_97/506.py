#!/usr/bin/env python
"""
Problem C. Recycled Numbers
Qualification Round 2012, Google Code Jam

14 April 2012

"""
import logging
import sys
import time


def setup_parser():
    from optparse import OptionParser
    usage = 'usage: %prog [options] <input file>'
    parser = OptionParser(usage=usage)
    parser.add_option('-v', '--verbose', dest='verbose', action='count',
                      help='increase verbosity')
    parser.add_option('-s', '--string', dest='string', action='store_true',
                      help='use string manipulation')
    return parser


def setup_logging(options):
    log_level = logging.WARNING
    if options.verbose == 1:
        log_level = logging.INFO
    elif options.verbose >= 2:
        log_level = logging.DEBUG
    logging.basicConfig(level=log_level)


def recycled_num(n, limit=sys.maxint):
    """Return a list of recycled numbers.

    m is a recycled number of n, and n < m <= limit.

    """
    result = []
    s = str(n)
    k = len(s)
    for i in range(1, k):
        if s[k - i] is not '0':
            p = 10**i
            r = n % p
            q = n / p
            m = q + r * 10**(k - i)
            if n < m and m <= limit:
                result.append(m)
    return set(result)


def recycled_str(n, limit=sys.maxint):
    result = []
    s = str(n)
    k = len(s)
    for i in range(1, k):
        if s[i] is not '0':
            m = int(s[i:] + s[:i])
            if n < m and m <= limit:
                result.append(m)
    return set(result)


def compute(line, method='numeric'):
    ts = time.time()
    a = line[0]
    b = line[1]

    if method is 'numeric':
        recycled = recycled_num
    else:
        recycled = recycled_str

    result = 0
    n = a
    while n < b:
        result += len(recycled(n, b))
        n += 1

    delta = time.time() - ts
    logging.info('%f s' % delta)
    return result


def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = setup_parser()
    options, args = parser.parse_args()
    setup_logging(options)

    if len(args) < 1:
        parser.print_help()
        return 2

    try:
        with open(args[0], 'r') as f:
            lines = [line.strip() for line in f.readlines()]
    except IOError, err:
        print >>sys.stderr, err
        return 1

    if options.string:
        method = 'string'
    else:
        method = 'numeric'

    t = int(lines.pop(0))
    for i in range(t):
        ins = [int(s) for s in lines[i].split()]
        print 'Case #%d: %s' % (i + 1, compute(ins, method))

    return 0


if __name__ == '__main__':
    sys.exit(main())
