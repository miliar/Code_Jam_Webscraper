#!/usr/bin/python

import sys

def line():
    return sys.stdin.readline()[:-1]

def readList():
    return map(eval,line().split())

def permutations(i,j):
    """Returns all the permutations of the list [i..j]"""
    if i == j:
        result = [[i]]
    else:
        result = []
        temp = permutations(i+1,j)
        for k in range(j-i+1):
            for p in temp:
                result.append((p[:k] if k > 0 else []) + [i] + (p[k:] if k < len(p) else []))
    return result

def permute(p,l):
    return [l[p[x]] for x in range(len(l))]

def findLowestWithGreaterOnTheRight(N):
    # N is a list of chars
    minimum = chr(ord('9') + 1)
    minPos = -1
    for i in range(len(N)):
        if any([N[i] < N[j] for j in range(i+1,len(N))]):
            if i > minPos:
                minPos = i
                minimum = N[i]
    return (minPos,minimum)


def findLeftmost(N,char):
    for i in range(len(N)):
        if N[len(N) - i - 1] == char:
            break
    return len(N) - i - 1

if __name__ == '__main__':
    numberOfCases = eval(line())
    for caseNumber in range(numberOfCases):
        N = eval(line())
        digits = list(str(N))

        # We compute the result of adding a 0
        lowest = sorted(list(str(N)))
        i = 0
        while lowest[i] == '0':
            i = i + 1
        temp = lowest[0]
        lowest[0] = lowest[i]
        lowest[i] = temp
        addAZero = [lowest[0], "0"] + lowest[1:]
        
        (minPos,char) = findLowestWithGreaterOnTheRight(digits)
        if minPos != -1:
            #print (minPos,char)
            #print digits
            smallestGreater = ([i for i in range(minPos+1,len(digits)) if digits[i] > char])[-1]
            lmg = smallestGreater
            smallestGreater = digits[lmg]
            digits[minPos] = smallestGreater
            digits[lmg] = char
            N = digits[:minPos+1] + sorted(digits[minPos+1:])
        else:
            N = addAZero
        print "Case #" + str(caseNumber+1) + ":",eval(''.join(N))
