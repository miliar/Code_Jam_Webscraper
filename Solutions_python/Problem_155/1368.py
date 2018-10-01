import os


inp = open('a.in').readlines()
t = int(inp[0])


def solve(case):
    r = l = 0
    p, s = case.split(' ')
    for idx in range(int(p) + 1):
        if idx > l:
            r += idx - l
            l += idx - l

        l += int(s[idx])

    return r

for idx in range(t):
    print('Case #%d: %d' % (idx + 1, solve(inp[idx + 1])))