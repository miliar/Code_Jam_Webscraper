#!/usr/bin/python2
import sys
import multiprocessing
import logging
import os
import itertools
import math
import gmpy2
import copy
import collections
import string
import scipy.stats as stats
from itertools import chain, combinations

class memoize:
    # from http://avinashv.net/2008/04/python-decorators-syntactic-sugar/
    def __init__(self, function):
        self.function = function
        self.memoized = {}

    def __call__(self, *args):
        try:
            return self.memoized[args]
        except KeyError:
            self.memoized[args] = self.function(*args)
            return self.memoized[args]

@memoize
def trielen(strings):
    trie = set()
    for s in strings:
        for l in range(1, len(s)+1):
            trie.add(s[:l])
    tl = len(trie)+1
    return tl

def solve(casedata):
    """ Solve case """
    [N, S] = casedata
    # worst
    occur = collections.Counter()
    for parts in uniq_subsets(k_subset(S, N)):
        ttl = sum([trielen(p) for p in parts])
        occur[ttl] += 1
    worst = max(occur)
    proba = occur[max(occur)] * math.factorial(N)
    # proba
    return "%d %d" % (worst, (proba % 1000000007))



#http://codereview.stackexchange.com/questions/1526/finding-all-k-subset-partitions
def k_subset(s, k):
    if k == len(s):
        return (tuple([(x,) for x in s]),)
    k_subs = []
    for i in range(len(s)):
        partials = k_subset(s[:i] + s[i + 1:], k)
        for partial in partials:
            for p in range(len(partial)):
                k_subs.append(partial[:p] + (partial[p] + (s[i],),) + partial[p + 1:])
    return k_subs

def uniq_subsets(s):
    u = set()
    for x in s:
        t = []
        for y in x:
            y = list(y)
            y.sort()
            t.append(tuple(y))
        t.sort()
        u.add(tuple(t))
    return u


def parse():
    """ Returns a list of N lists containing imput data for each case """
    t = int(sys.stdin.readline())
    cases = list()
    for case in range(t):
        M, N = map(int, sys.stdin.readline().rstrip('\n').split(' '))
        S = list()
        for s in range(M):
            S.append(sys.stdin.readline().rstrip('\n'))
        casedata = [N, S]
        cases.append(casedata)
    return cases

if __name__ == '__main__':
    cases = parse()
    #p = multiprocessing.Pool(multiprocessing.cpu_count())
    #results = p.map(solve, cases)
    #for case, result in enumerate(results):
    #    print('Case #%d: %s' % (case + 1, result))
    #    sys.stdout.flush()

    #for case, data in enumerate(cases):
    #    result = solve(data)
    #    print('Case #%d: %s' % (case + 1, result))
    #    sys.stdout.flush()

    p = multiprocessing.Pool(multiprocessing.cpu_count())
    resultobjs = [p.apply_async(solve, [case]) for case in cases]
    for case, resultobj in enumerate(resultobjs):
        print('Case #%d: %s' % (case + 1, resultobj.get()))
        sys.stdout.flush()
