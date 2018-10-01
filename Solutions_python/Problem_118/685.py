#! /usr/bin/pypy

import math

def solve(A,B):
    #find relevant indices in "fair" array
    minn = math.sqrt(A)
    maxx = math.sqrt(B)

    count = 0

    for fair in fairNumbers:
        if fair >= minn and fair <= maxx: #this one might be in the club
            sq = fair**2
            if A <= sq and B >= sq and isFair(sq):
                count += 1

    return count

def processFile(filename):
    f = open(filename, "r")
    resultFile = open("result.txt","w")

    T = int(f.readline()) #number of cases
    print "Solving %s cases:"%(T,)

    #read the other lines
    solutions = []
    for i,line in enumerate(f.readlines()):
        s =  map(int,line.strip().split(" ")) #split one line, convert to int
        A = s[0]
        B = s[1]

        a = "Case #%s: %s"%(i+1,solve(A,B)) #solution line
        solutions.append(a)
        print a

    resultFile.write("\n".join(map(str,solutions)))

    resultFile.close()
    f.close()

def rekk(pos, length): #pos starts at 1 here
    middle = length/2 + length%2
    even = (length%2 == 0)

    if pos == 1: #exclude zeros
        r = range(1,10)
    else:
        r = range(0,10)

    for i in r:
        if pos == middle and even:
            yield "%s%s"%(i,i)
        elif pos == middle and not even:
            yield "%s"%(i,)
        else:
            for j in rekk(pos+1,length):
                yield "%s%s%s"%(i,j,i)

def isFair(number):
    s = str(number)
    length = len(s)

    for i in range(length/2+1): #exclude the middle number if not even
        if s[i] != s[length-(1+i)]:
            return False
    return True

if __name__ == "__main__":
    # generate ALL the square numbers which might yield fair and square
    fairNumbers = []
    for i in range(1,8):
        for fair in rekk(1,i):
            fairNumbers.append(int(fair))

    print "Dun preoprocessin"

    while True:
        print "Input filename to solve:"
        fileNameToSolve = raw_input()
        processFile(fileNameToSolve)

        print "Results have been written to result.txt"
