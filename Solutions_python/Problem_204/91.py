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
inputFileName = "B-large.in"
outputFileName = inputFileName[:-3] + ".out"

startTime = time.time()
print startTime


def check1(N, rec, kit):
    v = kit
    q1 = (10 * v) / (9 * rec)
    q2 = (10 * v) / (11 * rec)
    if (q2 * 11 * rec) < (10 * v):
        q2 += 1
    if (q1 < q2):
        return False

    return True


def check2(N, rec, kit1, kit2):
    kits = [kit1, kit2]
    if not check1(N, rec[0], kits[0]):
        return False
    if not check1(N, rec[1], kits[1]):
        return False

    qmi = -10000000
    qma = 10000000

    for i in xrange(N):
        v = kits[i]
        r = rec[i]
        q1 = (10 * v) / (9 * r)
        q2 = (10 * v) / (11 * r)
        if (q2 * 11 * r) < (10 * v):
            q2 += 1

        if (q1 < qma):
            qma = q1
        if (q2 > qmi):
            qmi = q2

    return (qmi <= qma)


def check(N, rec, kits):
    qmi = -10000000
    qma = 10000000

    for i in xrange(N):
        v = kits[i]
        r = rec[i]
        q1 = (10 * v) / (9 * r)
        q2 = (10 * v) / (11 * r)
        if (q2 * 11 * r) < (10 * v):
            q2 += 1

        if q1 < qma:
            qma = q1
        if q2 > qmi:
            qmi = q2

    return (qmi <= qma)


def solve2dumb(N, P, rec, arr):
    a = arr[0]
    b = arr[1]
    maxCnt = 0
    for bb in itertools.permutations(b):
        cnt = 0
        for i in xrange(P):
            if check2(N, rec, a[i], bb[i]):
                cnt += 1
        if cnt > maxCnt:
            if maxCnt != 0:
                print "!!!!!!!!!!!! old = {0}, new = {1}".format(maxCnt, cnt)
            print bb
            maxCnt = cnt

    return maxCnt


def calcSingleTest(f):
    line = f.readline()
    N = int(line.split()[0])
    P = int(line.split()[1])
    rec = []
    line = f.readline()
    rec = map(int, line.split())
    arr = []
    for i in xrange(N):
        line = f.readline()
        a = map(int, line.split())
        a.sort()
        arr.append(a)
    print rec
    print '-----'
    print '\n'.join(map(str, arr))
    print '-----'

    if N == 1:
        cnt = 0
        a = arr[0]
        for i in xrange(P):
            if check1(N, rec[0], a[i]):
                cnt += 1
        return cnt
    else:
        pos = [0] * N
        cnt = 0
        qq1 = [-10000000] * N
        qq2 = [10000000] * N
        end = False
        while True:
            qmi = -10000000
            qma = 10000000

            for i in xrange(N):
                if pos[i] >= P:
                    end = True
                    break
                v = arr[i][pos[i]]
                r = rec[i]
                q1 = (10 * v) / (9 * r)
                q2 = (10 * v) / (11 * r)
                if (q2 * 11 * r) < (10 * v):
                    q2 += 1

                qq1[i] = q1
                qq2[i] = q2
                if q1 < qma:
                    qma = q1
                if q2 > qmi:
                    qmi = q2
            if end:
                break
            if (qmi <= qma):
                cnt += 1
                qq1 = [-10000000] * N
                qq2 = [10000000] * N
                for i in xrange(N):
                    pos[i] += 1
            else:
                for i in xrange(N):
                    if (qq1[i] < qmi):
                        pos[i] += 1

        # if N == 2:
        #     dumbRes = solve2dumb(N, P, rec, arr)

        return cnt

    return -1


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
