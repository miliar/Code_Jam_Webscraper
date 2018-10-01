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


def solve(casedata):
    """ Solve case """
    [X, S] = casedata
    fs = sorted(S)
    i = 0
    j = len(S)-1
    res = 0
    while i <= j:
        if j == i:
            res += 1
            break
        M, m = (fs[j], fs[i])
        if M+m <= X:
            i += 1
            j -= 1
            res += 1
        else:
            j -= 1
            res += 1
    return res

def parse():
    """ Returns a list of N lists containing imput data for each case """
    t = int(sys.stdin.readline())
    cases = list()
    for case in range(t):
        N, X = map(int, sys.stdin.readline().rstrip('\n').split(' '))
        S = map(int, sys.stdin.readline().rstrip('\n').split(' '))
        casedata = [X, S]
        cases.append(casedata)
    return cases

if __name__ == '__main__':
    cases = parse()
    #p = multiprocessing.Pool(multiprocessing.cpu_count())
    #results = p.map(solve, cases)
    #for case, result in enumerate(results):
    #    print('Case #%d: %s' % (case + 1, result))
    #    sys.stdout.flush()

    for case, data in enumerate(cases):
        result = solve(data)
        print('Case #%d: %s' % (case + 1, result))
        sys.stdout.flush()

    #p = multiprocessing.Pool(multiprocessing.cpu_count())
    #resultobjs = [p.apply_async(solve, [case]) for case in cases]
    #for case, resultobj in enumerate(resultobjs):
    #    print('Case #%d: %s' % (case + 1, resultobj.get()))
    #    sys.stdout.flush()
