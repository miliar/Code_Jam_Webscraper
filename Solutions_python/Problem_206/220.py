#!/usr/bin/env python


def solve(d, sl):
    fl = [ [ int(k) for k in elt.split()] for elt in sl ]
    soll = [(d - elt[0]) / (elt[1] + 0.) for elt in fl ]
    return d / max (soll)

if __name__ == "__main__":
    import sys
    l = sys.stdin.readlines()
    c = int(l[0])
    l = l[1:]
    for i in range(1,c+1):
        d, n = [int(k) for k in l[0].split()]
        sl = l[1:n+1]
        l = l[n+1:]
        sol = solve(d, sl)
        print "Case #%d: %s" % (i, sol)
