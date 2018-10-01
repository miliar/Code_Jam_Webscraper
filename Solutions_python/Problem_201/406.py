import glob, pprint, pickle, os, time, sys
from copy import copy
from zope.interface.tests import odd
from numpy import array, sin, cos
import numpy as np
import itertools
import math
import itertools
import random
from collections import defaultdict




def solve(N,K):
    grps = [(N,1)]

    while True:
        # you split all biggest groups into 2 parts
        place, nr = grps.pop()
        maxim, minim = place/2, (place-1)/2
        if nr>=K:
            return maxim, minim
        else:
            grps.append((maxim, nr))
            grps.append((minim, nr))
            K -= nr


        testDict = defaultdict(int)
        for key, val in grps:
            testDict[key] += val
        grps = sorted(testDict.items())
        # print grps

output = ""
TIC = time.time()
with open(sys.argv[1] if len(sys.argv) > 1 else "default.in") as f:
    def read_ints():
        return [int(x) for x in f.readline().strip().split(' ')]
    def read_frac():
        return [int(x) for x in f.readline().strip().split('/')]
    def read_strs():
        return [x for x in f.readline().strip().split(' ')]
    def read_floats():
        return [float(x) for x in f.readline().strip().split(' ')]

    (numquestions,) = read_ints()
    for questionindex in xrange(numquestions):

        ### calculate answer ###
        N,K = read_ints()
        answer = solve(N,K)

        ### output ###
        answer_str = "Case #{}: {}".format(questionindex+1, " ".join([str(a) for a in answer]) if isinstance(answer, tuple) else answer)
        output += answer_str + '\n'
        print answer_str

ofile = open('output', 'w').write(output)
TOC = time.time()