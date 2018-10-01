#!/bin/python
import sys
#sys.stdin = file("sample.in")

def readint(): return int(raw_input())

def readints(): return [ int(x) for x in raw_input().split() ]

def solve(R, C, tmap):
    for r in range(R):
        for c in range(C):
            if tmap[r][c] == "#":
                if r == R-1 or c == C-1:
                    return "Impossible"
                if not tmap[r][c] == tmap[r+1][c] == tmap[r][c+1] == tmap[r+1][c+1] == "#":
                    return "Impossible"
                tmap[r][c] = "/"
                tmap[r+1][c] = "\\"
                tmap[r][c+1] = "\\"
                tmap[r+1][c+1] = "/"
                
    return "".join([ "".join(r)+"\n" for r in tmap ])[:-1]

if __name__ == "__main__":
    nt = readint()
    for i in range(nt):
        RC = readints()
        tmap = [ [ x for x in raw_input()] for _ in range(RC[0]) ]
        print "Case #%d:\n%s" % ( i+1, str(solve(RC[0],RC[1],tmap)))
