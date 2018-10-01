#!/usr/bin/python3

import collections


def solve():
    n, c, m = map(int, input().split())
    cs = [[] for _ in range(c)]
    for _ in range(m):
        pi, bi = map(int, input().split())
        cs[bi-1].append(pi)
    for x in cs:
        x.sort()
    cs.sort(key=lambda x: -len(x))
    old_len = len(cs[1])
    xxx = 1000000000
    while len(cs[0]) > len(cs[1]):
        cs[1].append(xxx)
    a = b = 0
    for i, x in enumerate(cs[0]):
        d = collections.Counter(cs[0][i:] + [x for x in cs[1] if x != xxx]).most_common(1)[0][0]
        a += 1
        for y in cs[1]:
            if y != x and y == d:
                cs[1].remove(y)
                break
        else:
            for y in cs[1]:
                if y != x:
                    cs[1].remove(y)
                    break
            else:
                for y in cs[1]:
                    if y != 1:
                        b += 1
                        cs[1].remove(y)
                        break
                else:
                    a += 1
    return "%d %d" % (a, b)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        print('Case #%d: %s' % (i+1, solve()))
