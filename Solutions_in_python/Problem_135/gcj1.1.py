#!/usr/bin/env python

import sys

def main():
    T = int(sys.stdin.readline())
    for case in range(1,T+1):
        doCase(case)

def doCase(case):
    firstLine = getPossibleList()
    secondLine = getPossibleList()
    f = firstLine.split()
    s = secondLine.split()
    comm = [i for i in f if i in s]
    if len(comm) == 1:
        sys.stdout.write("Case #{}: {}\n".format(case, comm[0]))
    elif len(comm) == 0:
        sys.stdout.write("Case #{}: Volunteer cheated!\n".format(case))
    else:
        sys.stdout.write("Case #{}: Bad magician!\n".format(case))
    

def getPossibleList():
    ans = int(sys.stdin.readline())
    for i in range(1,5):
        if i == ans:
            goodLine = sys.stdin.readline()
        else:
            sys.stdin.readline()
    return goodLine



if __name__ == '__main__':
    main()
