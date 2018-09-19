from __future__ import print_function
import collections
import heapq
import math
import sys

f = sys.stdin

if len(sys.argv) > 1:
    f = open(sys.argv[1], "rt")

# 1, i, j, k
# 1, 2, 3, 4

# 0 is unused
mul_table = [
  [0,  0,  0,  0,  0],
  [0,  1,  2,  3,  4],
  [0,  2, -1,  4, -3],
  [0,  3, -4, -1,  2],
  [0,  4,  3, -2, -1],
]

value_table = {
  'i': 2,
  'j': 3,
  'k': 4,
}

def sgn(x):
    if x > 0: return 1
    elif x < 0: return -1
    else: return 0

def qmul(a, b):
    return sgn(a) * sgn(b) * mul_table[abs(a)][abs(b)]

T = int(f.readline().strip())


def calc(all):
    cur = 1
    fwd_table = [0]
    for x in all:
        cur = qmul(cur, value_table[x])
        fwd_table.append(cur)

    cur = 1
    rev_table = [0]
    for x in reversed(all):
        cur = qmul(value_table[x], cur)
        rev_table.append(cur)
    rev_table.reverse()

    #~ print(fwd_table)
    #~ print(rev_table)

    n = len(all)

    for a in range(1, n-1):
        if fwd_table[a] != 2:  # Not i - skip.
            continue
        middle = 1
        for b in range(a+1, n):
            middle = qmul(middle, value_table[all[b-1]])
            if middle == 3 and rev_table[b] == 4:
                return 'YES'

    return 'NO'

for case_id in range(1, T+1):
    L, X = map(int, f.readline().strip().split())
    chars = f.readline().strip()
    #~ print(L, X, chars)

    r = calc(chars * X)

    print(str.format('Case #{0}: {1}', case_id, r))
