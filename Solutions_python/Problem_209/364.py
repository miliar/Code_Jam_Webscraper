from math import pi
from decimal import getcontext, Decimal


def sol(n, k, ris, his):
    pancakes = sorted([(ri, hi) for ri, hi in zip(ris, his)], key=lambda x: (-x[0], -x[1]))
    best = 0.0
    for i in xrange(n - k + 1):
        cri, chi = pancakes[i]
        stuff = sorted([(hi, ri) for ri, hi in pancakes[(i + 1):]], key=lambda x: x[0] * x[1] * 2 * pi, reverse=True)[:(k - 1)]
        curr = cri ** 2 *  pi + 2 * cri * pi * chi
        for hi, ri in stuff:
            curr += 2 * ri * pi * hi
        best = max(curr, best)

    return best


def show(i, val):
    print "Case #%s: %.15f" % (i, val)


if __name__ == "__main__":
    T = int(raw_input().strip())
    getcontext().prec = 15

    for i in xrange(1, T + 1):
        n, k = map(int, raw_input().strip().split())
        ris, his = [], []
        for _ in xrange(n):
            ri, hi = map(int, raw_input().strip().split())
            ris.append(ri)
            his.append(hi)
        show(i, sol(n, k, ris, his))
   
