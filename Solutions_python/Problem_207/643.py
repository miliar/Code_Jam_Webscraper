import sys
import os
import math
from itertools import product
from copy import deepcopy
from collections import defaultdict


negates =  {
    'R' : ['R', 'O', 'V'],
    'O' : ['R', 'O', 'Y'],
    'Y' : ['O', 'Y', 'G'],
    'G' : ['Y', 'G', 'B'],
    'B' : ['V', 'G', 'B'],
    'V' : ['V', 'R', 'B']
}

compliments = dict([
    (k, list(set(negates) - set(negates[k])))
        for k in negates 
])


sys.setrecursionlimit(100000)

def check_fail(cols, path_started):
    total = sum(cols.values())
    if total > 5:
        for s in cols:
            if cols[s] > ((total + path_started)/ 2):
                return True


def find_ham_cycle(cols, path=[]):
    if (sum(cols.values()) == 0):
        if (path[-1] in compliments[path[0]]):
            return path
        else:
            return None

    if check_fail(cols, bool(path)):
        return None

    # print(cols, check_fail(cols))

    for next_col in reversed(sorted(cols.keys(), key = lambda x : cols[x])):
        if cols[next_col] < 1:
            return None

        if not len(path) or next_col in compliments[path[-1]]:
            cols[next_col] -= 1
            npath = find_ham_cycle(cols, path + [next_col])
            cols[next_col] += 1

            if npath is not None:
                return npath
    return None


def solve(N, R, O, Y, G, B, V):
    cols = {
        'R' : R,
        'O' : O,
        'Y' : Y,
        'G' : G,
        'B' : B,
        'V' : V
    }


    # print(cols)
    path = find_ham_cycle(cols)

    if path is not None:
        return ''.join(path)
    else:
    	return  'IMPOSSIBLE'
    

def line():
    return sys.stdin.readline().strip()

def write_solution(i, ans):
    sys.stdout.write(
        'Case #%s: %s\n' % (i, ans)
    )


if __name__ == '__main__':
    count = int(line())

    for i in range(count):
        N, R, O, Y, G, B, V = map(int, line().split())
        write_solution(i + 1, solve(N, R, O, Y, G, B, V))
        


