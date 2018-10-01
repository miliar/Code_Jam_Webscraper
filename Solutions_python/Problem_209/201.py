ncase = int(input())

import math
from decimal import *

def area(r,h):
    st = Decimal(math.pi) * r * r
    ss = 2 * Decimal(math.pi) * r *h
    return st, ss, st+ss

for case in range(1, ncase+1):
    n, k = [int(s) for s in input().split(" ")]

    cakes = []
    for i in range(n):
        r, h = [int(s) for s in input().split(" ")]
        cakes.append(area(r,h))

    cakes.sort(key=lambda x: x[2], reverse=True)
    # print(cakes)

    j = 0
    final_area = 0
    max_top = 0
    while(j < k):
        # print(j, k, final_area)
        # print(len(cakes), cakes)
        if final_area == 0:
            final_area += cakes[0][2]
            max_top = cakes[0][0]
            del cakes[0]
        else:
            max_delta = 0
            max_i = 0
            for i in range(len(cakes)):
                if cakes[i][0] > max_top:
                    delta = cakes[i][0] - max_top + cakes[i][1]
                else:
                    delta = cakes[i][1]
                if delta > max_delta:
                    max_delta = delta
                    max_i = i
            # print(i)
            final_area += max_delta
            if cakes[max_i][0] > max_top:
                max_top = cakes[max_i][0]
            del cakes[max_i]
        j += 1

    print("Case #{}: {:.9f}".format(case, final_area))

    # print(d2)

