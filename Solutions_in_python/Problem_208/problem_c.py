# import heapq  # @UnresolvedImport
from collections import defaultdict  # @UnresolvedImport
from sys import stdin


def main():
    t = int(stdin.readline().strip())
    for k in xrange(1, t+1):
        n, q = (int(s) for s in stdin.readline().strip().split(' '))
        i_e_s = [[i] + [int(s) for s in stdin.readline().strip().split(' ')]
               for i in xrange(n)]
        # matrix[i][j]: distance i to j
        matrix = [[int(s) for s in stdin.readline().strip().split(' ')]
                  for _ in xrange(n)]
        _u_v = [[int(s) for s in stdin.readline().strip().split(' ')]
                for _ in xrange(q)]
        best = dict()
        for i, e, s in sorted(i_e_s, key=lambda i_e_s: -i_e_s[2]):
            j = i
            d = 0
            while j+1 < n:
                d += matrix[j][j+1]
                if d > e:
                    break
                if (i, j+1) not in best:
                    best[(i, j+1)] = d/float(s)
                j += 1
        times = defaultdict(lambda: 999999999999999.9)
        times[0] = 0
        for i in xrange(n):
            for j in xrange(i+1, n):
                if (i, j) in best:
                    # print "times[{}] = min({}, {}+{}) = {}, {}".format(j, times[j], times[i], best[(i, j)], min(times[j], times[i] + best[(i, j)]), n)
                    times[j] = min(times[j], times[i] + best[(i, j)])
        print "Case #{}: {}".format(k, times[n-1])

main()
