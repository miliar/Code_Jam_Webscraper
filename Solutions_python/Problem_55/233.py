#!/usr/bin/python

import sys
import os.path

if len(sys.argv) < 2:
    print('themePark.py file')
    exit(0)

infile = sys.argv[1]
try:
    input = open(infile, 'r')
except:
    raise('error opening the file')
nbTestCaseTxt = input.readline()
try:
    nbTestCase = int(nbTestCaseTxt)
except:
    raise('incorrect format for the number of test case')
testCases = list()
try:
    for i in range(nbTestCase):
        (r, k, n) = input.readline().split()
        r = int(r)
        k = int(k)
        n = int(n)
        groups = input.readline().split()
        if len(groups) != n:
            raise('wrong number of groups')
        for i in range(len(groups)):
            groups[i] = int(groups[i])
        testCases.append({ 'r':r, 'k':k, n:'n', 'q':groups })
except ValueError:
    raise('incorrect format for a test case')
except:
    raise('wrong number of test cases')

for i in range(len(testCases)):
    testCase = testCases[i]
    r = testCase.get('r')
    k = testCase.get('k')
    n = testCase.get('n')
    q = testCase.get('q')
    res = 0
    for j in range(r):
        seatedPeople = 0
        endOfQueue = list()
        while len(q) > 0:
            groupSize = q[0]
            if seatedPeople + groupSize > k:
                break
            seatedPeople += groupSize
            endOfQueue.append(q.pop(0))
        res += seatedPeople
        q.extend(endOfQueue)
    print('Case #%d: %d' % (i + 1, res))
