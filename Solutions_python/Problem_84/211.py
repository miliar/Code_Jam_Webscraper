#!/usr/bin/python
import sys

def solve(d, R, C):

    for r in range(R-1):
        fst = True
        for c in range(C-1):
            if d[r][c] == "#" and \
               d[r][c+1] == "#" and \
               d[r+1][c] == "#" and \
               d[r+1][c+1] == "#":
                d[r][c] = "/"
                d[r][c+1] = "\\"
                d[r+1][c] = "\\"
                d[r+1][c+1] = "/"
            elif d[r][c] != "#":
                pass
            else:
                return "Impossible"
    str = '\n'.join([''.join(r) for r in d])
    if "#" in str:
        return "Impossible"
    return str

T = int(sys.stdin.readline())

for t in range(T):
    line = sys.stdin.readline()
    R, C = [int(x) for x in line.split()]
    rows = []
    for r in range(R):
        line = sys.stdin.readline()
        rows.append([x for x in line.strip()])
    sol = solve(rows, R, C)

    print "Case #" + str(t+1) + ":"
    print sol
