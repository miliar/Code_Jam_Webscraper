#!/usr/bin/python

import sys

def case(S, p, ts):
    good = 0
    for t in ts:
        if t in [0,1,29,30]:
            if t >= p:
                good += 1
        else:
            base = t // 3
            mod = t % 3
            if base + min(1, mod) >= p:
                good += 1
            elif S > 0 and base + max(1, mod) >= p:
                S -= 1
                good += 1
    return good

def main():
    T = int(next(sys.stdin))
    for x in xrange(1, T+1):
        N, S, p, ts = next(sys.stdin).split(None, 3)
        N, S, p = map(int, (N, S, p))
        ts = map(int, ts.split())
        print "Case #%d: %s" % (x, case(S, p, ts))

main()
