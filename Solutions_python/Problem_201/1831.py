from collections import defaultdict
from functools import lru_cache


@lru_cache(maxsize=None)
def prepare(N):
    if N == 0:
        # If no stalls left empty, we have no choices
        return []
    if N == 4:
        # 4 is special in some way
        return [((2, 1), 1), ((1, 0), 1), ((0, 0), 2)]
    choices = []
    rem = (N - 1) // 2
    if (N % 2) == 0:
        # We have two middle options
        choices.append(((rem, rem + 1), 1))
        # if (rem % 2) == 0:
        #     choices.append(((rem // 2, rem // 2), 1))
        #     choices += prepare(rem)
        #     rec = prepare(rem // 2)
        #     for ((a, b), c) in rec:
        #         choices.append(((a, b), c * 2))
        choices += prepare(rem)
        choices += prepare(rem + 1)
    else:
        # We have one middle option
        choices.append(((rem, rem), 1))
        rec = prepare(rem)
        for ((a, b), c) in rec:
            choices.append(((a, b), c * 2))
    return choices


def combine(arr):
    res = defaultdict(lambda: 0)
    for ((a, b), v) in arr:
        res[min(a, b), max(a, b)] += v
    return res


def choices(N):
    return combine(prepare(N))


def solve(N, K):
    chc = choices(N)
    used = 0
    for k in (reversed(sorted(chc.keys()))):
        cnt = chc[k]
        used += cnt
        if used >= K:
            return "{} {}".format(k[1], k[0])

if __name__ == "__main__":
    T = int(input())
    for I in range(1, T+1):
        n, k = [int(x) for x in input().split()]
        print("Case #{}: {}".format(I, solve(n, k)))
