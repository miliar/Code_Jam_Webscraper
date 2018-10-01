import math
import psyco
psyco.full()

def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def best(l):
    if len(l) == 0:
        return 0.0

    if len(l) == 1:
        return l[0][2]

    if len(l) == 2:
        rr = dist(l[0], l[1]) + l[0][2] + l[1][2]
        return rr / 2.0

    assert False

def solve():
    for case in xrange(input()):
        n = int(raw_input())
        pl = []
        for _ in xrange(n):
            x, y, r = [int(s) for s in raw_input().split()]
            pl += [(x, y, r)]

        if len(pl) == 1:
            R = pl[0][2]
        else:
            R = None
            for k in xrange(1 + (2 ** n)):
                a = []
                b = []
                for i in xrange(n):
                    if k % (2 ** i) == 0:
                        a += [pl[i]]
                    else:
                        b += [pl[i]]

                if len(a) == 0 or len(b) == 0:
                    continue

                Rc = max(best(a), best(b))
                if R is None or Rc < R:
                    R = Rc

        res = R
        print 'Case #%d: %.6f' % (case+1, res)

solve() # so that psyco can do its magic
