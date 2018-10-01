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

def lcm(a,b):
    return a*b/gcd(a,b)

def allgcd(l):
    ret = l[0]
    for x in l[1:]:
        ret = gcd(ret, x)
    return ret

def alllcm(l):
    ret = l[0]
    for x in l[1:]:
        ret = lcm(ret, x)
    return ret

def solve(L,H,notes):
    notes.sort()
    lnotes = len(notes)

    #print L, H, notes
    for i in range(0, len(notes)+1):
        before = notes[:i]
        after = notes[i:]

        if len(before) == 0:
            blcm = 1
        else:
            blcm = alllcm(before)

        if len(after) == 0:
            agcd = int((H+blcm-1)/blcm)*blcm
        else:
            agcd = allgcd(after)

        #print "@",i, blcm, agcd

        if blcm <= agcd and gcd(blcm,agcd) == blcm:
            term = agcd/blcm
            for x in range(1, term+1):
                if gcd(x,term) == x or len(after) == 0:
                    if L <= blcm*x <= H:
                        return blcm*x

    return "NO"

if __name__ == "__main__":
    nt = readint()
    for i in range(nt):
        N,L,H = tuple(readints())
        notes = readints()
        print "Case #%d: %s" % ( i+1, str(solve(L,H,notes)))
