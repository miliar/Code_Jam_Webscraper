from solver import solver
from functools import lru_cache
from collections import Counter


@lru_cache(maxsize=None)
def build(n):
    if n == 0:
        return Counter()
    a, b = (n-1) // 2, n // 2
    return Counter([n]) + build(a) + build(b)


def find(counter, k):
    for key, value in sorted(counter.items(), reverse=True):
        if k <= value:
            return key
        k -= value


@solver
def bathroom(lines):
    n, k = map(int, lines[0].split())
    v = find(build(n), k)
    mini, maxi = (v-1) // 2, v // 2
    return '{} {}'.format(maxi, mini)


if __name__ == '__main__':
    bathroom.from_cli()
