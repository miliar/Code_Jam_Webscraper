#!/usr/bin/env python
# vim: set fileencoding=utf-8
'''Module docstring
Template version: 1.2

Problem

It's opening night at the opera, and your friend is the prima donna (the lead
female singer). You will not be in the audience, but you want to make sure she
receives a standing ovation -- with every audience member standing up and
clapping their hands for her.

Initially, the entire audience is seated. Everyone in the audience has a
shyness level. An audience member with shyness level Si will wait until at
least Si other audience members have already stood up to clap, and if so, she
will immediately stand up and clap. If Si = 0, then the audience member will
always stand up and clap immediately, regardless of what anyone else does. For
example, an audience member with Si = 2 will be seated at the beginning, but
will stand up to clap later after she sees at least two other people standing
and clapping.

You know the shyness level of everyone in the audience, and you are prepared to
invite additional friends of the prima donna to be in the audience to ensure
that everyone in the crowd stands up and claps in the end. Each of these
friends may have any shyness value that you wish, not necessarily the same.
What is the minimum number of friends that you need to invite to guarantee a
standing ovation?
Input

The first line of the input gives the number of test cases, T. T test cases
follow. Each consists of one line with Smax, the maximum shyness level of the
shyest person in the audience, followed by a string of Smax + 1 single digits.
The kth digit of this string (counting starting from 0) represents how many
people in the audience have shyness level k. For example, the string "409"
would mean that there were four audience members with Si = 0 and nine audience
members with Si = 2 (and none with Si = 1 or any other value). Note that there
will initially always be between 0 and 9 people with each shyness level.

The string will never end in a 0. Note that this implies that there will always
be at least one person in the audience.

Output

For each test case, output one line containing "Case #x: y", where x is the
test case number (starting from 1) and y is the minimum number of friends you
must invite.

Limits

1 ≤ T ≤ 100.
Small dataset

0 ≤ Smax ≤ 6.

Large dataset

0 ≤ Smax ≤ 1000.

Input

    Output

     4
     4 11111
     1 09
     5 110011
     0 1

     Case #1: 0
     Case #2: 1
     Case #3: 2
     Case #4: 0
     In Case #1, the audience will eventually produce a standing ovation on its
     own, without you needing to add anyone -- first the audience member with
     Si = 0 will stand up, then the audience member with Si = 1 will stand up,
     etc.

     In Case #2, a friend with Si = 0 must be invited, but that is enough to
     get the entire audience to stand up.

     In Case #3, one optimal solution is to add two audience members with Si =
     2.

     In Case #4, there is only one audience member and he will stand up
     immediately. No friends need to be invited.
'''

# for python2
from __future__ import division, print_function

VERSION = '%(prog)s 1.0'

import argparse
import sys
import os
import functools
import logging
#import heapq
#from operator import itemgetter
#from collections import defaultdict
#from collections import deque
#from array import array
#from bisect import bisect
#from math import sqrt

# for interactive call: do not add multiple times the handler
if 'LOG' not in locals():
    LOG = None
LOG_LEVEL = logging.ERROR
FORMATER_STRING = ('%(asctime)s - %(filename)s:%(lineno)d - '
                   '%(levelname)s - %(message)s')

def configure_log(level=LOG_LEVEL, log_file=None):
    'Configure logger'
    if LOG:
        LOG.setLevel(level)
        return LOG
    log = logging.getLogger('%s log' % os.path.basename(__file__))
    if log_file:
        handler = logging.FileHandler(filename=log_file)
    else:
        handler = logging.StreamHandler(sys.stderr)
    log_formatter = logging.Formatter(FORMATER_STRING)
    handler.setFormatter(log_formatter)
    log.addHandler(handler)
    log.setLevel(level)
    return log

LOG = configure_log()

# to be used as decorator so no capitalisation
# pylint: disable=invalid-name
class memoized(object):
    '''Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    '''
    # pylint: disable=too-few-public-methods
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
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)
# pylint: enable=invalid-name

class CommentedFile(object):
    'Implements comments skip for file'
    # pylint: disable=too-few-public-methods
    def __init__(self, in_file, commentstring='#'):
        self.in_file = in_file
        self.commentstring = commentstring
    def next(self):
        'The next line but skips comments'
        line = self.in_file.next()
        while line.startswith(self.commentstring):
            line = self.in_file.next()
        return line
    def __iter__(self):
        return self

def parse_levels(level_string):
    '''Return a mapping of level strings
    Keys are shyness levels
    Values are nb of people

    >>> levels = parse_levels('409')
    >>> levels[0]
    4
    >>> levels[2]
    9
    '''
    levels = dict((k, int(v)) for k, v in enumerate(level_string))
#    for key, value in levels.items():
#        if value == 0:
#            levels.pop(key)
    return levels

def nb_friends_required(levels):
    '''Return the min nb of friends required to have everybody standup
    '''
    total_friends = 0
    total_standing = 0
    for shyness_level in levels:
        nb_persons = levels[shyness_level]
        if nb_persons == 0:
            continue
        nb_friends = 0
        if total_standing < shyness_level:
            nb_friends = shyness_level - total_standing
        total_friends += nb_friends
        total_standing += nb_persons + nb_friends
    return total_friends

def do_job(in_file, out_file=sys.stdout):
    'Do the work'
    # sticking with names used in gcj
    # pylint: disable=invalid-name
    LOG.debug('Start working with files: %s and %s',
              in_file.name, out_file.name)
    # first line is number of test cases
    T = int(in_file.readline())
    for testcase in range(T):
        #N = int(in_file.readline())
        # for integer input
        #values = [int(x) for x in in_file.readline().split()]
        # for other inputs
        values = in_file.readline().split()
        assert len(values) == 2
        s_max = int(values[0])
        assert len(values[1]) == s_max + 1
        levels = parse_levels(values[1])
        result = nb_friends_required(levels)
        print_output(out_file, testcase, result)

def print_output(out_file, testcase, result):
    'Formats and print result'
    print('Case #%d:' % (testcase + 1), end=' ', file=out_file)
    print(result, file=out_file)
    #print('%.6g' % result, file=out_file)

def create_parser():
    'Return the argument parser'
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version=VERSION)
    parser.add_argument('--debug', dest='debug', action='store_true',
                        help=argparse.SUPPRESS)
    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument('-q', '--quiet', '--silent', dest='quiet',
                           action='store_true', default=False,
                           help='run as quiet mode')
    verbosity.add_argument('-v', '--verbose', dest='verbose',
                           action='store_true', default=False,
                           help='run as verbose mode')
    parser.add_argument('-t', dest='template', action='store_true',
                        default=False,
                        help=('template name for construct'
                              'out file name as in_file.out (default False)'))
    parser.add_argument('-w', dest='out_file',
                        help=('output file or stdout if FILE is - '
                              '(default case) or TEMPLATE.out (default if '
                              'template is given)'))
    #type=argparse.FileType('w')
    parser.add_argument('in_file', help='input file (default stdin)',
                        default=sys.stdin, type=argparse.FileType('r'))
    return parser

def main(argv=None):
    'Program wrapper'
    if argv is None:
        argv = sys.argv[1:]
    parser = create_parser()
    args = parser.parse_args(argv)
    if args.verbose:
        LOG.setLevel(logging.INFO)
    if args.quiet:
        LOG.setLevel(logging.CRITICAL)
    if args.debug:
        LOG.setLevel(logging.DEBUG)
#    # unset verbose for easy option check
#    args.verbose = False
#    if not any(args.__dict__.values()):
#        parser.error('Must provide at least one option')
    if args.template and not args.out_file:
        args.out_file = ''.join((args.in_file.name, '.out'))
    if not args.out_file or args.out_file == '-':
        out_file = sys.stdout
    else:
        try:
            out_file = open(args.out_file, 'w')
        except IOError:
            parser.error('Problem opening file: %s' % args.out_file)
    sys.setrecursionlimit(2**30-1)
    do_job(args.in_file, out_file)
    return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())

