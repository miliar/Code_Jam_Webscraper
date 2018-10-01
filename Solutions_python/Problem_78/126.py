#!/bin/python
import sys
#sys.stdin = file("sample.in")

def readint(): return int(raw_input())

def readints(): return [ int(x) for x in raw_input().split() ]

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def solve(ints):
    N = ints[0]
    Pd = ints[1]
    Pg = ints[2]

    out = [100,0]

    judge = True
    if Pg in out:
        judge = Pd == Pg

    if judge:
        judge = (100/gcd(100-Pd,Pd)) <= N

    if judge:
        return "Possible"
    else:
        return "Broken"

if __name__ == "__main__":
    nt = readint()
    for i in range(nt):
        cs = readints()
        print "Case #%d: %s" % ( i+1, str(solve(cs)))
