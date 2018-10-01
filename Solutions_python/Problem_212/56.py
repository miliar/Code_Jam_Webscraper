from collections import *
# from itertools import *
# from heapq import *


def solve(P, G):
    N = len(G)
    print N, P, G
    G = [i % P for i in G]
    if P == 2:
        return G.count(0) + (G.count(1) + 1) / 2
    if P == 3:
        r0 = G.count(0)
        r1 = G.count(1)
        r2 = G.count(2)
        return G.count(0) + min(r1, r2) + (abs(r1 - r2) + 2) / 3
    if P == 3:
        r0 = G.count(0)
        r1 = G.count(1)
        r2 = G.count(2)
        return G.count(0) + min(r1, r2) + (abs(r1 - r2) + 2) / 3
    if P == 4:
        r0 = G.count(0)
        r1 = G.count(1)
        r2 = G.count(2)
        r3 = G.count(3)
        res = r0 + r2 / 2 + min(r1, r3)
        r2 %= 2
        r5 = abs(r1 - r3)
        if r2 == 0:
            res += (r5 + 3) / 4
        else:
            if r5 >= 2:
                res += 1
                r5 -= 2
                res += (r5 + 3) / 4
            else:
                res += 1
        return res


def main():
    T = int(fi.readline().strip())
    for i in xrange(T):
        N, P = map(int, fi.readline().strip().split())
        G = map(int, fi.readline().strip().split())
        res = solve(P, G)
        out = "Case #%d: %s\n" % (i + 1, res)
        print out
        fo.write(out)

fi = open('A-large.in', 'r')
fo = open('A-large.out', 'w')
main()
fi.close()
fo.close()

# print solve(4, [1, 1, 1, 1, 1, 1, 3])
