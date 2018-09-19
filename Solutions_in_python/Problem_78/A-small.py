#!/usr/bin/env python


def solve(n, pd, pg):
    for d in xrange(1, n+1):
        if d*pd % 100 != 0:
            continue
        wt = d*pd/100

        if pg == 0:
            return wt == 0

        for g in xrange(d, 200001):
            if g*pg % 100 == 0:
                wo = g*pg/100 - wt
                if 0 <= wo <= g - d:
                    #print 'solve(%d, %d, %d): wt = %d, wo = %d, d = %d, g = %d' % (n, pd, pg, wt, wo, d, g)
                    return True

    return False
        

if __name__ == '__main__':
    import fileinput
    inp = fileinput.input()
    t = int(inp.readline())
    for i in xrange(1, t+1):
        n, pd, pg = map(int, inp.readline().split())
        can = 'Possible' if solve(n, pd, pg) else 'Broken'
        print 'Case #%d: %s' % (i, can)
