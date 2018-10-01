#!/usr/bin/python3

from copy import deepcopy


def cal(mp, N):
    count = 0
    n = 0
    for r in range(len(mp)):
        for c in range(len(mp[0])):
            if mp[r][c]:
                n += 1
                if r < len(mp)-1 and mp[r][c] == mp[r+1][c]:
                    count += 1
                if c < len(mp[0])-1 and mp[r][c] == mp[r][c+1]:
                    count += 1
    if n != N:
        return (mp, 40000)
    return (deepcopy(mp), count)


def test(mp, r, c, N):
    if r == len(mp):
        return cal(mp, N)
    rr, cc = r, (c+1) % len(mp[0])
    if cc == 0:
        rr += 1
    mp[r][c] = False
    m, res = test(mp, rr, cc, N)
    mp[r][c] = True
    mm, re = test(mp, rr, cc, N)
    if re < res: res, m = re, mm
    return m, res


T = int(input())

for t in range(1, T+1):
    R, C, N = [int(i) for i in input().split()]
    mp = [[False]*C for i in range(R)]
    mp, res = test(mp, 0, 0, N)
    print('Case #%d: %d' % (t, res))
    """
    for r in mp:
        for i in r:
            print('%d' % i, end='')
        print()
    """
