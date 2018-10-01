#!/usr/bin/python

def solve(L, P, C):
    pts = 0
    while L<P:
        L *= C
        pts += 1

    steps = 0
    val = 1
    while val<pts:
        val *= 2
        steps += 1

    return steps

if __name__ == "__main__":
    t = int(raw_input())
    for i in range(1, t+1):
        line = raw_input();
        tri = line.split(" ")
        L = int(tri[0])
        P = int(tri[1])
        C = int(tri[2])
        print "Case #" + str(i) + ": " + str(solve(L, P, C))

