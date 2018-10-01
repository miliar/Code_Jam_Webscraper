from collections import defaultdict
from multiprocessing import Pool

def f(nk):
    i = nk[0]
    n = nk[1]
    k = nk[2]
    empty = range(1, n + 1)
    occupied = [0, n + 1]
    maxmaxlr = 0
    maxminlr = 0

    if n == k:
        return "Case #{0}: {1} {2}".format(i, 0, 0)

    for j in xrange(k):  # for each person
        minlr = defaultdict(int)
        maxlr = defaultdict(int)
        for e in empty:  # for each empty stall, compute Ls and Rs
            ls = n + 2
            rs = n + 2
            for o in occupied:
                if e > o and e - o - 1 < ls:
                    ls = e - o - 1
                if e < o and o - e - 1 < rs:
                    rs = o - e - 1
                minlr[e] = min(ls, rs)
                maxlr[e] = max(ls, rs)
        maxminlr = max(minlr.values())
        maxminlrlist = []
        maxmaxlr = 0

        for e in minlr.keys():
            if minlr[e] == maxminlr:
                maxminlrlist.append(e)
                if maxlr[e] > maxmaxlr:
                    maxmaxlr = maxlr[e]

        pick = n + 2
        for e in maxminlrlist:
            if maxlr[e] == maxmaxlr and e < pick:
                pick = e

        empty.remove(pick)
        occupied.append(pick)
    return "Case #{0}: {1} {2}".format(i, maxmaxlr, maxminlr)

if __name__ == '__main__':
    t = int(raw_input())  # read a line with a single integer
    nklist = list()
    for i in xrange(1, t + 1):
        n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
        nk = (i,n,k)
        nklist.append(nk)
    p = Pool(24)
    ret = p.map(f, nklist)
    for r in ret:
        print r
