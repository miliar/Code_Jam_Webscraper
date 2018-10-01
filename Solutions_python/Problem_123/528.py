# Test input
inputCase = "small"
problem = "A" # A, B, C...
inputFile = open(problem + "-" + inputCase + "-attempt2.in")
outputFile = open(problem + "-" + inputCase + ".out", "w")
# Template code

import math
import sys
import random
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
    result = "Case #" + str(i) + ": " + result
    print result
    f.write(result + "\n")

# Solver code
def readCase(f):
    a, n = readInts(f)
    return [a, n, readInts(f)]

def solve(solverFunction, inputFile, outputFile):
    cases = readInt(inputFile)
    for i in range(cases):
        case = readCase(inputFile)
        result = solverFunction(case)
        writeCase(outputFile, i + 1, result)

def recurse(a, ans, nums):
    if not nums:
        return ans
    x = nums[0]
    if x < a:
        return recurse(a + x, ans, nums[1:])
    else:
        if a == 1:
            return recurse(a, ans + 1, nums[1:])
        else:
            return min(recurse(2 * a - 1, ans + 1, nums), recurse(a, ans + 1, nums[1:]))

def solver(case):
    a, n, nums = case
    nums.sort()
    return str(recurse(a, 0, nums))

solve(solver, inputFile, outputFile)
