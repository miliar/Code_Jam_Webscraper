# python 3.6
import numpy as np
import math
# import networkx as nx
import fractions
from functools import reduce
import time
import itertools
import collections
# from networkx_viewer import Viewer
import fileinput
import multiprocessing

use_multiprocessing = False
impossible = 'IMPOSSIBLE'
epsilon = 1e-10



def read():
    n, p = next_ints()
    G = next_ints()
    return n, p, G

def solve(inp):
    n, p, G = inp
    r = list(map(lambda x: x%p, G))
    rs = [0] * p
    for x in r:
        rs[x] += 1
    res = 0
    if p==2:
        res = rs[0] + (rs[1]+1)//2
    if p==3:
        m12 = min(rs[1], rs[2])
        res = rs[0]
        res += m12
        rs[1] -= m12
        rs[2] -= m12
        res += (rs[1]+2)//3
        res += (rs[2]+2)//3
    if p==4:
        m13 = min(rs[1], rs[3])
        q1 = max(rs[1], rs[3])
        res = rs[0]
        res += m13
        q1 -= m13
        res += rs[2] // 2
        q2 = rs[2] % 2
        if q2 == 0:
            res += (q1 + 3) // 4
        else:
            res += (q1 + 5) // 4



    return res

def helper(n, p):
    return


def main():
    t = next_int()  # read a line with a single integer

    if use_multiprocessing:
        inputs = []
        for case_number in range(1, t + 1):
            inputs.append(read())
        k = multiprocessing.cpu_count()
        p = multiprocessing.Pool(k)
        outputs = list(p.map(solve, inputs))
        for case_number, res in enumerate(outputs):
            print("Case #{}: {}".format(case_number + 1, res))

    else:
        for case_number in range(1, t + 1):
            case_input = read()
            case_result = solve(case_input)
            print("Case #{}: {}".format(case_number, case_result))


def is_in_map(i, j, m, n):
    return 0 <= i < m and 0 <= j < n


def create_file_line_iterator():
    for line in fileinput.input():
        yield line


def next_line():
    return next(fileLineIterator).strip()


def next_int():
    next_ints_line = next_line().split()
    return [int(s) for s in next_ints_line] if len(next_ints_line) > 1 else int(next_ints_line[0])


def next_ints():
    next_ints_line = next_line().split()
    return [int(s) for s in next_ints_line]


class MyFraction(object):
    def __init__(self, n, d):
        if d == 0:
            self.npa = np.nan
        else:
            gcd = math.gcd(n, d)
            gcd *= 1 if d > 0 else -1
            n1, d1 = n // gcd, d // gcd
            self.npa = np.array([n1, d1], dtype=np.int64)

    def __eq__(self, other):
        return self.npa[0] == other.npa[0] and self.npa[1] == other.npa[1]

    def __cmp__(self, other):
        r = self.npa[0] * other.npa[1] - self.npa[1] * other.npa[0]
        if r < 0:
            return -1
        if r > 0:
            return 1
        return 0

    def __lt__(self, other):
        return self.npa[0] * other.npa[1] - self.npa[1] * other.npa[0] < 0

    def __le__(self, other):
        return self.npa[0] * other.npa[1] - self.npa[1] * other.npa[0] <= 0


fileLineIterator = create_file_line_iterator()
if __name__ == '__main__':
    main()
