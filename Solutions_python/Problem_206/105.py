import glob, pprint, pickle, os, time, sys
from copy import copy
from operator import itemgetter
from numpy import array, sin, cos
import numpy as np
import itertools
import math

BIGINT = 10**128
import sys
sys.setrecursionlimit(10000)


def solve(D,horses):
    #1 when is the last horse at the finish line to find maximum speed
    times = []
    for horse in horses:
        time_to_finish = 1.*(D - horse[0]) / horse[1]
        times.append(time_to_finish)

    #2 do I hit any horse starting


    return 1.*D/max(times)




output = ""
TIC = time.time()
with open(sys.argv[1] if len(sys.argv) > 1 else "default.in") as f:
    def read_ints():
        return [int(x) for x in f.readline().strip().split(' ')]
    def read_frac():
        return [int(x) for x in f.readline().strip().split('/')]
    def read_strs():
        return [x for x in f.readline().strip().split(' ')]
    def read_chrs():
        return [x for x in f.readline().strip()]
    def read_floats():
        return [float(x) for x in f.readline().strip().split(' ')]

    (numquestions,) = read_ints()
    for questionindex in xrange(numquestions):

        ### calculate answer ###
        D,N = read_ints()
        horses = []
        for n in xrange(N):
            horses.append(read_ints())
        answer = solve(D,horses)

        ### output ###
        answer_str = "Case #%d: %.7f" % (questionindex+1, answer)
        output += answer_str + '\n'
        print answer_str

ofile = open('output', 'w').write(output)
TOC = time.time()