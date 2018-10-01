#!/usr/bin/env python

import sys

def line():
    return sys.stdin.readline()[:-1]

def readPattern(s):
    pattern = []
    i = 0
    while i < len(s):
        if s[i] == "(":
            until = s.find(")",i)
            pattern.append(s[i+1:until])
            i = until
        else:
            pattern.append(s[i])
        i = i + 1
    return pattern

if __name__ == "__main__":
    L,D,N = map(eval,line().split())
    words = []
    for i in range(D):
        words.append(line())

    for i in range(N):
        pattern = map(set,readPattern(line()))
        numberOfValidWords = 0
        for word in words:
            isGoodCandidate = True
            for j in range(L):
                if word[j] not in pattern[j]:
                    isGoodCandidate = False
                    break
            if isGoodCandidate:
                numberOfValidWords = numberOfValidWords + 1
        print "Case #" + str(i+1) + ": " + str(numberOfValidWords)
