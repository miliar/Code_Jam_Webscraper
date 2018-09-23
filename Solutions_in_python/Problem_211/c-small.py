"""
http://networkx.readthedocs.io/en/networkx-1.11/tutorial/index.html
https://docs.python.org/3/library/re.html
https://docs.python.org/3/library/math.html
https://docs.python.org/3/library/collections.html
https://docs.python.org/3/library/itertools.html
https://docs.python.org/3/library/functools.html#functools.lru_cache
"""

# import numpy as np
# import networkx as nx
# import re
# import math
# import time  # start_time = time.time(); elapsed_time = time.time() - start_time
# from collections import Counter
# from collections import OrderedDict
# from collections import deque
# from queue import PriorityQueue  # q = PriorityQueue(); q.put((pr1, pr2, ...)); item = q.get()
# from itertools import combinations
# from itertools import permutations
# from functools import lru_cache  # @lru_cache(maxsize=None)
# from copy import copy, deepcopy
# from sys import stdin, stdout
# from sys import maxsize  # 9 * 10**18
# inf = float('inf')

def main():
    caseCount = int(input())
    for caseIdx in range(1, caseCount + 1):
        # read an integer
        N, K = map(int, input().strip().split(' '))
        U = float(input())
        P = list(map(float, input().strip().split(' ')))

        ans = solve(N, K, U, P)

        print("Case #{}: {}".format(caseIdx, ans))


def solve(N, K, U, P):
    # print(N, K, U, P)

    P.sort()
    P.append(1)
    # print(P)
    for i in range(len(P)-1):
        if U <= 0:
            break
        diff = P[i+1] - P[i]
        need = diff * (i + 1)
        if need <= U:
            for j in range(i+1):
                P[j] += diff
            U -= need
            continue
        else:
            for j in range(i+1):
                P[j] += U / (i+1)
            U = 0

    # print(P)

    prob = 1
    for p in P:
        prob *= p
    return prob


if __name__ == '__main__':
    main()
