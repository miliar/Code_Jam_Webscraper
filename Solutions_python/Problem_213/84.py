import itertools
import time
import operator
# import collections
from collections import Counter
from fractions import gcd
from random import randint
import random

inputFileName = "test.in"
inputFileName = "B-small-attempt0.in"
# inputFileName = "B-small-attempt1.in"
# inputFileName = "B-small-attempt2.in"
# inputFileName = "B-small-attempt3.in"
# inputFileName = "B-large.in"
outputFileName = inputFileName[:-3] + ".out"

startTime = time.time()
print startTime


def calcSingleTest(f):
    line = f.readline()
    N = int(line.split()[0])
    C = int(line.split()[1])
    M = int(line.split()[2])
    arr = []

    cc = [0] * C
    tcp = []
    for i in xrange(C):
        tcp.append([0] * N)

    for i in xrange(M):
        line = f.readline()
        p = int(line.split()[0])
        b = int(line.split()[1])
        tcp[b - 1][p - 1] += 1
        cc[b - 1] += 1

    print cc
    print tcp
    agg = dict()

    # print tcp
    for i in xrange(C):
        agg[i] = Counter(tcp[i])
        print agg[i]
    rides = 0
    proms = 0
    if (C == 2):
        r0 = max(cc[0], cc[1])
        r1 = tcp[0][0] + tcp[1][0]
        mr = max(r0, r1)
        rides = mr
        half = mr / 2
        for i in xrange(1, N):
            s = tcp[0][i] + tcp[1][i]
            if s > mr:
                if (proms != 0):
                    raise AssertionError("AAA " + str(proms))
                proms = s - mr

        pass
    else:
        raise AssertionError("AAA " + str(N))

    return "{0} {1}".format(rides, proms)


with open(inputFileName) as inpF:
    with open(outputFileName, 'w') as outF:
        line = inpF.readline()
        testsCount = int(line)
        for i in xrange(1, testsCount + 1):
            print '--------  {0}/{1} {2} --------------------------'.format(i, testsCount, (time.time() - startTime))
            res = calcSingleTest(inpF)
            print '--------  {0}/{1} {2} --------------------------'.format(i, testsCount, (time.time() - startTime))
            print ' '
            outF.write('Case #{0}: {1}\n'.format(i, res))
            outF.flush()

print "Finished!!!! Total time = {0}".format((time.time() - startTime))
