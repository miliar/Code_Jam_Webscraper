import sys
import math

name = "A-small"
path = ""

path2 = '/Users/daniel/Downloads/C-small-1-attempt0'

sys.stdin = open(path2 +'.in')
sys.stdout = open(path2 + ".out", "w")

testCases = int(input())

sys.setrecursionlimit(15000)


def find_largest(subspaces, k):
    max_sp = max(subspaces)
    index_max_sp = subspaces.index(max_sp)
    right_sp = int(max_sp/2)
    left_sp = int(max_sp/2) -1 if max_sp % 2 == 0 else right_sp
    subspaces = subspaces[0: index_max_sp] + [left_sp] + [right_sp] + subspaces[index_max_sp+1: len(subspaces)]
    if k == 1:
        return max(left_sp, right_sp), min(left_sp, right_sp)
    return find_largest(subspaces, k-1)





for testCase in range(1, testCases + 1):
    size, k = str(input()).split()

    x, y = find_largest([int(size)], int(k))
    print('Case #{}: {} {}'.format(testCase, x, y))


