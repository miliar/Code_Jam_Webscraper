from __future__ import (print_function,
                        division,
                        unicode_literals)
from bisect import bisect_left, bisect_right
MAX_LN = 55


def dfs(s, v, m):
    if m == 2:
        v -= 2 * int(s) ** 2
        if v < 0:
            r = []
        else:
            r = [s + s]
        return r
    elif m == 1:
        v -= int(s) ** 2
        if v < 0:
            return []
        else:
            return [s]
    else:
        v -= 2 * int(s) ** 2
        if v < 0:
            return []
        r = []
        r.extend(map(lambda t: s + t + s, dfs('0', v, m - 2)))
        r.extend(map(lambda t: s + t + s, dfs('1', v, m - 2)))
        r.extend(map(lambda t: s + t + s, dfs('2', v, m - 2)))
        r.extend(map(lambda t: s + t + s, dfs('3', v, m - 2)))
        return r[:]

nums = []
for i in xrange(1, MAX_LN):
    nums.extend(dfs('1', 9, i))
    nums.extend(dfs('2', 9, i))
    nums.extend(dfs('3', 9, i))
nums = map(lambda x: int(x) ** 2, nums)
T = input()
for t in xrange(T):
    l, r = map(int, raw_input().split())
    print('Case #{0}: '.format(t + 1), end='')
    print((bisect_right(nums, r) - bisect_left(nums, l)))
