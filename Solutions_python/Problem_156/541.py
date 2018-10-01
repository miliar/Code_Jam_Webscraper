#!/usr/bin/env python
import sys

case_num = 1
def printres(result):
    global case_num
    print "Case #%s: %s" % (case_num, result)
    case_num += 1

def readline(): 
    return sys.stdin.readline().rstrip('\n')
def splitline(f):
    return map(f, readline().split())


def solve():
    readline()
    plates = splitline(int)
    best = 10**10
    for i in range(1, max(plates)+1):
        moves = 0
        for p in plates:
            moves += (p-1) / i
        best = min(best, moves + i)
    printres(best)

def main():
    for i in range(int(readline())): 
        solve()

if __name__ == '__main__': 
    main()

