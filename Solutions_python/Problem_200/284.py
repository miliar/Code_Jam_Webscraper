# coding: utf-8
import copy
def construct(arr):
    res = 0
    for i in arr:
        res = 10 * res + i
    return res


def check(arr):
    return arr == sorted(arr)


def solve():
    N = input()
    length = len(N)
    N = int(N)
    res = [0 for _ in range(length)]
    for i in range(length):
        tmp = copy.deepcopy(res)
        for j in range(10):
            tmp[i:length] = [j for _ in range(i, length)]
            if check(tmp) and construct(tmp) <= N:
                res[i:length] = [j for _ in range(i, length)]

    return construct(res)

T = int(input())
for tc in range(T):
    res = solve()
    print('Case #{}: {}'.format(tc + 1, res))
