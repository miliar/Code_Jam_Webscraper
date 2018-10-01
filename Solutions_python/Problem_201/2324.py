import sys
import math
import itertools
# from sortedcontainers import SortedList
import heapq

# def brute(N, K):
#     filled = SortedList([0, N+1])
#     for _k in xrange(K):
#         maximin, maximax = -1, -1
#         maximin_meta = None
#         for _n in xrange(1, N+1):
#             if _n not in filled:
#                 nloc = filled.bisect(_n)
#                 ls = _n - filled[nloc-1] - 1
#                 rs = filled[nloc] - _n - 1

#                 m = min(ls, rs)
#                 if m > maximin:
#                     maximin = m 
#                     maximin_meta = SortedList([(max(ls, rs), min(ls, rs), _n)])
#                 elif m == maximin:
#                     maximin_meta.add((max(ls, rs), min(ls, rs), _n))

#         filled.add(maximin_meta[-1][2])
#         if _k == K-1:
#             return maximin_meta[-1][:2]


def clever(N, K):
    # gaps = SortedList([N])
    gaps = [-N]
    for i in range(K-1):
        g = -heapq.heappop(gaps)
        if g % 2 == 1:
            heapq.heappush(gaps, -(g // 2))
            heapq.heappush(gaps, -(g // 2))
        else:
            heapq.heappush(gaps, -(g // 2))
            heapq.heappush(gaps, -(g // 2 - 1))
    g = -heapq.heappop(gaps)
    mi = g // 2
    ma = g // 2
    if g % 2 == 0: mi-=1
    return ma, mi


def main(infile, outfile):

    with open(infile) as inf:
        with open(outfile, 'w') as outf:
            test_case = 1
            t = int(inf.readline())
            for line in inf.readlines():
                N, K = map(int, line.split())
                print("Case {} N {} K {}".format(test_case, N, K))

                # Brute force
                ma, mi = clever(N, K)
                # print "Clever", ma, mi
                # ma2, mi2 = brute(N, K)
                # print "Brute", ma2, mi2
                # assert (ma, mi) == (ma2, mi2)

                print("Case #{}: {} {}".format(test_case, ma, mi))
                outf.write("Case #{}: {} {}".format(test_case, ma, mi))
                if t != test_case:
                    outf.write('\n')
                test_case += 1

if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]

    main(infile, outfile)
