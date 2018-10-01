#!/usr/bin/python

import re
import sys

def tokenise(case):
    tokens = []

    withinBrackets = False;
    token = []

    for c in case:
        if withinBrackets:
            if c == ')':
                withinBrackets = False;
                tokens.append(token)
                token = []
            else:
                token.append(c)
        elif c == '(':
            withinBrackets = True;
        else:
            tokens.append([c])

    return tokens

def findNumCases(case, wordLen, allWords):
    tokens = tokenise(case)

    regex = ''
    for token in tokens:
        tokenRegex = '['
        for possibleLetter in token:
            tokenRegex = tokenRegex + possibleLetter
        tokenRegex = tokenRegex + ']'
        regex = regex + tokenRegex

    regex = re.compile(regex) 

    numMatches = 0
    for word in allWords:
        if regex.match(word) != None:
            numMatches = numMatches + 1

    return numMatches

inFile = open(sys.argv[1], 'r')

ldnLine = inFile.readline()
ldnLine = ldnLine.strip()
wordLen, numWords, numCases = ldnLine.split(' ')
wordLen = int(wordLen)
numWords = int(numWords)
numCases = int(numCases)
# print wordLen, numWords, numCases

allWords = []
for i in range(numWords):
    allWords.append(inFile.readline().strip());
# print allWords

allCases = []
for i in range(numCases):
    allCases.append(inFile.readline().strip());
# print allCases

inFile.close()
inFile = None

for i in range(len(allCases)):
    case = allCases[i]
    numCases = findNumCases(case, wordLen, allWords[:])
    print "Case #" + str(i + 1) + ":", str(numCases)
