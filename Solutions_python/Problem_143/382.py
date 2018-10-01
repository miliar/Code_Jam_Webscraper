import itertools
import time
import operator
#import collections
from collections import Counter

#inputFileName = "test.in"
inputFileName = "B-small-attempt0.in"
#inputFileName = "B-small-attempt1.in"
#inputFileName = "B-small-attempt2.in"
#inputFileName = "B-small-attempt3.in"
#inputFileName = "B-large.in"
outputFileName = inputFileName[:-3] + ".out"

startTime = time.time()
print startTime


def calcSingleTest(f):
    line = f.readline()
    A = int(line.split()[0])
    B = int(line.split()[1])
    K = int(line.split()[2])
    cnt = 0
    for a in xrange(A):
        for b in xrange(B):
            x = a & b
            if x < K:
                cnt +=1
    return cnt


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