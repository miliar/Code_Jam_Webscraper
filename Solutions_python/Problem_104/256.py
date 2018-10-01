#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# Author: Yuande <miraclecome (at) gmail.com>


import sys
import itertools

class RedirectStdoutTo(object):
    def __init__(self, out_new):
        self.out_new = out_new

    def __enter__(self):
        self.out_old = sys.stdout
        sys.stdout = self.out_new

    def __exit__(self, *args):
        sys.stdout = self.out_old

class RedirectStdinTo(object):
    def __init__(self, in_new):
        self.in_new = in_new 

    def __enter__(self):
        self.in_old = sys.stdin
        sys.stdin = self.in_new

    def __exit__(self, *args):
        sys.stdin = self.in_old


def control(inf, outf='b.txt'):
    with open(inf, mode='r') as fdin, open(outf, mode='w') as fdout:
        with RedirectStdinTo(fdin), RedirectStdoutTo(fdout):

            for tc in xrange(1, int(sys.stdin.readline())+1):
                line = [int(w) for w in sys.stdin.readline().rstrip('\n').split()]
                N, S = line[0], line[1:]
                content = [( i, {i} ) for i in S]
                result = []
                exist_flag = 0
                for i in xrange(2, N):
                    if exist_flag: break
                    for subset in itertools.combinations(S, i):
                        if exist_flag: break
                        total = sum(subset)
                        subset = set(list(subset))
                        for j, item in enumerate(content):
                            if total in item:
                                if not item[1] & subset:
                                    result = (subset, item[1])
                                    exist_flag = 1
                                    break
                        else:
                            content.append( (total, subset) )

                print 'Case #%d:' % (tc, )
                if exist_flag:
                    print ' '.join([str(i) for i in result[0]])
                    print ' '.join([str(i) for i in result[1]])
                else:
                    print 'Impossible'

if __name__ == '__main__':
    control(sys.argv[1])
