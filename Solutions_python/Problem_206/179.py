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
# from itertools import combinations
# from itertools import permutations
# from functools import lru_cache
# from sys import stdin, stdout


def main():
    caseCount = int(input())
    for caseIdx in range(1, caseCount + 1):
        D, N = map(int, input().strip().split(' '))

        Ks = []
        Ss = []
        for i in range(N):
            Ki, Si = map(int, input().strip().split(' '))
            Ks.append(Ki)
            Ss.append(Si)

        ans = solve(D, N, Ks, Ss)

        print("Case #{}: {}".format(caseIdx, ans))


def solve(D, N, Ks, Ss):
    ts = [(D-Ks[i])/Ss[i] for i in range(N)]
    maxT = max(ts)
    return '{:.6f}'.format(D/maxT)


if __name__ == '__main__':
    main()
