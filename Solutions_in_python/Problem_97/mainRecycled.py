#! /usr/bin/pypy

import cPickle as pickle

def isRecycled(n,m):
    fingerprintN = fingerprints[n]
    fingerprintM = fingerprints[m]

    if len(fingerprintN) != len(fingerprintM):
        return False

    l = len(fingerprintN)

    for i in range(l):
        if fingerprintN[0] == fingerprintM[i]:
            flag = True
            for j in range(1,l):
                if fingerprintN[j] != fingerprintM[(i+j)%l]:
                    flag = False
                    break
            if flag:
                return True

    return False

def solve(A,B):
    result = 0

    for n in range(A,B+1):
        for m in range(n+1,B+1):
            if isRecycled(n,m):
                result += 1

    return result

def processFile(filename):
    f = open(filename, "r")
    resultFile = open("result.txt","w")

    N = int(f.readline()) #number of cases
    print "Solving %s cases"%(N,)

    #read the other lines
    solutions = [] 
    for i,line in enumerate(f.readlines()):
        (A,B) = map(int,line.split(" "))
        
        a = "Case #%s: %s"%(i+1,solve(A,B))
        solutions.append(a)
        print a
    
    resultFile.writelines(solutions)

if __name__ == "__main__":
    fingerprints = pickle.load(open("fingerprints.p","rb"))

    print solve(1,9)
    print solve(10,40)
    print solve(100,500)
    print solve(1111,2222)

    while True:
        print "Input filename to solve:"
        fileNameToSolve = raw_input()
        processFile(fileNameToSolve)

        print "Results have been written to result.txt"
