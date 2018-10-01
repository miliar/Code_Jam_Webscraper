# Test input
inputCase = "large"
problem = "A" # A, B, C...
inputFile = open(problem + "-" + inputCase + ".in")
outputFile = open(problem + "-" + inputCase + ".out", "w")
# Template code

import math
import numpy
import sys
sys.setrecursionlimit(1000000000)

def readLine(f):
    return next(f).strip()

def readInt(f, b=10):
    return int(readLine(f), b)

def readFloat(f):
    return float(readLine(f))

def readInts(f, b=10, splitter=' '):
    return [int(x, b) for x in readLine(f).split(splitter)]

def readFloats(f, splitter=' '):
    return [float(x) for x in readLine(f).split(splitter)]

def readWords(f):
    return readLine(f).split()

def writeCase(f, i, result):
    f.write("Case #" + str(i) + ": " + str(result) + "\n")

# Solver code
def readCase(f):
    [s_max, k] = readWords(f)
    return [int(s_max), k]

def solve(solverFunction, inputFile, outputFile):
    cases = readInt(inputFile)
    for i in range(cases):
        case = readCase(inputFile)
        result = solverFunction(case)
        writeCase(outputFile, i + 1, result)

def solver(case):
    s_max, k = case
    K = []
    for i in range(len(k)):
        K.append(int(k[i]))
    output = 0
    sum = K[0]
    for i in range(1, s_max+1):
        if sum < i:
            output += i - sum
            sum += i - sum
        sum += K[i]
    return output


solve(solver, inputFile, outputFile)
