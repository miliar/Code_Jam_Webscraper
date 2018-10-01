#!/usr/bin/env python3
import bisect


def mlen(s, val):
    p = bisect.bisect_left(s, val)
    return len(s) - p


def calc(n, m, data):
    lines, rows = [], []

    for i in range(n):
        l = list(set(data[i]))
        lines += [l]

    for i in range(m):
        l = list(set(data[j][i] for j in range(n)))
        rows += [l]

    for i in range(n):
        for j in range(m):
            if mlen(lines[i], data[i][j]) > 1 and mlen(rows[j], data[i][j]) > 1:
                return "NO"
    return "YES"


if __name__ == '__main__':
    cnt = int(input())
    for T in range(cnt):
        n, m = list(map(int, input().split()))
        text = list([list(map(int, input().split())) for i in range(n)])

        print("Case #{}: {}".format(T + 1, calc(n, m, text)))

