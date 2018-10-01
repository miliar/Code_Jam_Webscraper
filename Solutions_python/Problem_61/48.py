#!/usr/bin/python
import os, sys

def doPureCached(n):
    # These values were calculated from (longer) runs of doPure()
    answers = [0, 0, 1, 2, 3, 5, 8, 14, 24, 43, 77, 140, 256, 472, 874, 1628, 3045, 5719, 10780, 20388, 38674, 73562, 40265, 68060, 13335, 84884]
    return answers[n]

def isPure(n, S):
    # n is always in S
    lenS = len(S)
    cur = lenS + 1
    setS = set(S)
    while True:
        if cur == 1:
            #print S
            return True
        # we're looking for cur
        # it can't be more than cur-1 elements in since it starts at 2
        #location = binary_search(S, cur, 0, len(S))
        if cur not in setS:
            return False
        location = binary_search(S, cur, 0, min(cur, lenS))
        if (location == -1):
            return False
        cur = location + 1

def doPure(n):
    count = 0
    for S in genallsubsets(2, n):
        if isPure(n, S):
            count += 1
    # don't forget the empty subset
    return count + 1


def main(filename):
    fileLines = open(filename, 'r').readlines()
    index = 0
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        n = int(fileLines[index][:-1])
        index += 1
        #answer = doPure(n)
        answer = doPureCached(n)
        print "Case #%d: %d" % (caseNum + 1, answer % 100003)

def genallsubsets(min, max):
    S = [[i] for i in range(min, max)]
    for s in S:
        yield s
    N = S
    for k in range(min, max):
      if N:
           S = N
           N = []
           for e in S:
             for i in range(e[-1]+1,max):
                f = e[:]
                f.append(i)
                yield f
                N.append(f)      

def binary_search(a, x, lo, hi):
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return mid
    return -1


if __name__ == '__main__':
    main(sys.argv[1])
