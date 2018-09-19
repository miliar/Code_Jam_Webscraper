#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
"""Problem

Sean and Patrick are brothers who just got a nice bag of candy from their
parents. Each piece of candy has some positive integer value, and the children
want to divide the candy between them. First, Sean will split the candy into
two piles, and choose one to give to Patrick. Then Patrick will try to
calculate the value of each pile, where the value of a pile is the sum of the
values of all pieces of candy in that pile; if he decides the piles don't have
equal value, he will start crying.

Unfortunately, Patrick is very young and doesn't know how to add properly. He
almost knows how to add numbers in binary; but when he adds two 1s together, he
always forgets to carry the remainder to the next bit. For example, if he wants
to sum 12 (1100 in binary) and 5 (101 in binary), he will add the two rightmost
bits correctly, but in the third bit he will forget to carry the remainder to
the next bit:

  1100 + 0101 ------ 1001

So after adding the last bit without the carry from the third bit, the final
result is 9 (1001 in binary). Here are some other examples of Patrick's math
skills:

5 + 4 = 1
7 + 9 = 14
50 + 10 = 56

Sean is very good at adding, and he wants to take as much value as he can
without causing his little brother to cry. If it's possible, he will split the
bag of candy into two non-empty piles such that Patrick thinks that both have
the same value. Given the values of all pieces of candy in the bag, we would
like to know if this is possible; and, if it's possible, determine the maximum
possible value of Sean's pile.  Input

The first line of the input gives the number of test cases, T. T test cases
follow. Each test case is described in two lines. The first line contains a
single integer N, denoting the number of candies in the bag. The next line
contains the N integers Ci separated by single spaces, which denote the value
of each piece of candy in the bag.  Output

For each test case, output one line containing "Case #x: y", where x is the
case number (starting from 1). If it is impossible for Sean to keep Patrick
from crying, y should be the word "NO". Otherwise, y should be the value of the
pile of candies that Sean will keep.  Limits

1 ≤ T ≤ 100.
1 ≤ Ci ≤ 106.

Small dataset

2 ≤ N ≤ 15.

Large dataset

2 ≤ N ≤ 1000.

Sample

Input

2 5
1 2 3 4 5 3
3 5 6

Output

Case #1: NO
Case #2: 11
"""

from __future__ import division, print_function
from optparse import OptionParser
import sys
import functools
import logging
import operator
import itertools

def configure_log(log_file=None):
    "Configure the log output"
    log_formatter = logging.Formatter("%(asctime)s - %(filename)s:%(lineno)d - "
                                      "%(levelname)s - %(message)s")
    if log_file:
        handler = logging.FileHandler(filename=log_file)
    else:
        handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(log_formatter)
    LOG.addHandler(handler)

LOG = None
# for interactive call: do not add multiple times the handler
if not LOG:
    LOG = logging.getLogger('template')
    configure_log()

class memoized(object):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)
    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__
    def __get__(self, obj, objtype):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)

def pat_sum_pile(x):
    """Return the sum as binary add without retenue
    >>> pat_sum_pile([5, 12])
    9
    >>> pat_sum_pile([5, 4])
    1
    >>> pat_sum_pile([7, 9])
    14
    >>> pat_sum_pile([50, 10])
    56
    >>> pat_sum_pile([5, 6, 7])
    4
    """
    return reduce(operator.xor, x)

def sean_sum_pile(x):
    "Return the sum of the pile values"
    return reduce(operator.add, x)

def naive_process(values):
    """Return the max value Sean can keep without Pat to cry or NO
    Naive algo: quadratic time
    >>> naive_process([1, 2, 3, 4, 5])
    'NO'
    >>> naive_process([5, 6, 3])
    11
    >>> naive_process([5, 3, 6])
    11
    >>> naive_process([6, 5, 3])
    11
    >>> naive_process([3, 5, 6])
    11
    >>> naive_process([5, 6])
    'NO'
    >>> naive_process([5, 5])
    5
    """
    max_value = None
    nb_rounds = 0
    LOG.debug(len(values))
    if pat_sum_pile(values) != 0:
        # only if the total sum is 0 we can have a fair split for Pat
        # a ^ b ^ c == d ^e
        # implies
        # a ^ b ^ c ^ d ^ e == d ^ e ^ d ^ e => 0
        return 'NO'
    for i in xrange(1, len(values) // 2 + 1):
        for split in itertools.combinations(values, i):
            nb_rounds += 1
            complement = values[:]
            for value in split:
                if value in complement:
                    complement.remove(value)
            if pat_sum_pile(split) == pat_sum_pile(complement):
                max_value = max(max_value, max(sean_sum_pile(split),
                                               sean_sum_pile(complement)))
        if max_value:
            # as we take splits from smallest size, the first value should be
            # the highest because all prices are positive
            break
    LOG.debug(nb_rounds)
    if not max_value:
        max_value = 'NO'
    return max_value

def do_job(in_file, out_file):
    "Do the work"
    LOG.debug("Start working with files: %s and %s"
              % (in_file.name, out_file.name))
    # first line is number of test cases
    T = int(in_file.readline())
    for testcase in xrange(T):
        # for integer input
        N = int(in_file.readline())
        # for other inputs
        values = map(int, in_file.readline().split())
        assert len(values) == N
        result = naive_process(values)
        print_output(out_file, testcase, result)

def print_output(out_file, testcase, result):
    "Formats and print result"
    print("Case #%d:" % (testcase + 1), end=' ', file=out_file)
    print(result, file=out_file)

def main(argv=None):
    "Program wrapper."
    if argv is None:
        argv = sys.argv[1:]
    usage = "%prog [-v] [-w out_file] [-t] in_file"
    parser = OptionParser(usage=usage)
    parser.add_option("-t", dest="template", action="store_true", default=False,
                      help=("template name for construct"
                            "out file name as in_file.out (default False)"))
    parser.add_option("-w", dest="out_file",
            help=("output file or stdout if FILE is - (default case)"
                  "or TEMPLATE.out (default if template is given)"))
    parser.add_option("-v", "--verbose", dest="verbose",
            action="store_true", default=False,
            help = "run as verbose mode")
    (options, args) = parser.parse_args(argv)
    if not args:
        parser.error('no input file given')
    if options.verbose:
        LOG.setLevel(logging.DEBUG)
    if args[0] == '-':
        in_file = sys.stdin
    else:
        try:
            in_file = open(args[0], 'r')
        except IOError:
            parser.error("File, %s, does not exist." % args[0])
    if options.template and not options.out_file:
        options.out_file = ''.join((args[0], '.out'))
    if not options.out_file or options.out_file == '-':
        out_file = sys.stdout
    else:
        try:
            out_file = open(options.out_file, 'w')
        except IOError:
            parser.error("Problem opening file: %s" % options.out_file)
    sys.setrecursionlimit(2**31-1)
    do_job(in_file, out_file)
    return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())
