#!/usr/bin/env python3
import sys
from heapq import *

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, q = [int(s) for s in input().split(" ")]
    e = []
    s = []
    for j in range(n):
        e_j, s_j = [int(s) for s in input().split(" ")]
        e.append(e_j)
        s.append(s_j)
    d = []
    for j in range(n):
        d.append([int(s) for s in input().split(" ")])

    results = []
    for j in range(q):
        u, v = [int(s) - 1 for s in input().split(" ")];
        #print("start {}, end {}".format(u, v))
        visited = [[False for _ in range(n)] for __ in range(n)]

        h = [] # heap queue
        # initialise queue
        heappush(h, (0, (u, u, e[u])))
        # we have visited city u with horse u
        visited[u][u] = True

        while len(h) > 0:
            t, (num, steed, energy) = heappop(h)
            #print("Visiting city {} with steed {} with energy {} at time {}"
                    #.format(num, steed, energy, t))
            visited[num][steed] = True

            if num == v:
                results.append(t)
                break

            # else explore neighbours that have not already been visited
            for k in range(n):
                if not visited[k][steed]:
                    dist = d[num][k]
                    if dist > 0 and dist <= energy:
                        # (time, (city_number, steed_number, steed_energy))
                        # don't swap steed
                        heappush(h, (t + dist / s[steed], (k, steed, energy - dist)))
                        # do swap steed
                        heappush(h, (t + dist / s[steed], (k, k, e[k])))

    print("Case #{}: {}".format(i, " ".join([str(x) for x in results])))
    sys.stdout.flush()
# check out .format's specification for more formatting options
