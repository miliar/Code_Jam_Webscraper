#!/usr/bin/python
import sys

def tuples():
    result = []
    for i in range(0,3):
        for k in range(0,3):
            result.append((i,k))
    return result

def validTriples():
    result = []
    l = tuples()
    for i in l:
        for j in l:
            for k in l:
               if (i[0] + j[0] + k[0]) % 3 == 0 and (i[1] + j[1] + k[1]) % 3 == 0:
                   result.append((i,j,k))
    return result

def count(x,l):
    result = 0
    for y in l:
        if x == y:
            result = result + 1
    return result

def processTriple(triple,modularTrees):
    numbers = {}
    a = {}
    for t in triple:
        numbers[t] = 0
        a[t] = modularTrees[t]
        
    for t in triple:
        numbers[t] = numbers[t] + 1
    if len(numbers.keys()) == 1: # We have only one distinct pair
        return a[t] * (a[t] - 1) * (a[t] - 2)
    elif len(numbers.keys()) == 2: # We have two distinct pairs
        if numbers[triple[0]] == 2:
            return a[triple[0]] * (a[triple[0]] - 1) * a[triple[1]]
        else:
            return a[triple[1]] * (a[triple[1]] - 1) * a[triple[0]]
    else: # We have three distinct pairs
        return a[triple[0]] * a[triple[1]] * a[triple[2]]

def solve(modularTrees):
    result = 0
    for t in validTriples():
        result = result + processTriple(t,modularTrees)
    return result
    
if __name__ == '__main__':
    next = sys.stdin.readline
    numberOfCases = int(next())
    for caseNumber in range(1,numberOfCases+1):
        # Process a case
        D = {} # Utility dictionary
        
        # Read a whole line of parameters
        case = map(int,next().split())
        n,A,B,C,D,x0,y0,M = case

        trees = []
        X,Y = x0,y0
        trees.append((X,Y))
        for i in range(1,n):
            X = (A*X+B) % M
            Y = (C*Y+D) % M
            trees.append((X,Y))
        modularTrees = {}
        for k in range(0,3):
            for j in range(0,3):
                modularTrees[(k,j)] = 0
        for i in trees:
            modularTrees[(i[0]%3,i[1]%3)] = modularTrees[(i[0]%3,i[1]%3)] + 1

        print "Case #" + str(caseNumber) + ": " + str(solve(modularTrees)/6)
