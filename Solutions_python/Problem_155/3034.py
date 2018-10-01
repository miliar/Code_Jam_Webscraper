#!/usr/bin/python

import sys

inputFile = open(sys.argv[1], 'r')
outputFile = open(sys.argv[2], 'w')
numTests = int(inputFile.readline())

def solveCase(line):
    "Solves one case. `line` is a string of input."
    tokens = line.split()
    standing = 0
    added = 0
    for i in range(0, int(tokens[0]) + 1):
        if (standing + added < i):
            added = added + 1
        standing = standing + int(tokens[1][i])
    return str(added)

for i in range(0, numTests):
    outputFile.write("Case #" + str(i + 1) + ": ")
    outputFile.write(solveCase(inputFile.readline()))
    outputFile.write("\n")
