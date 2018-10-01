#!/usr/bin/env pypy3
"""Task #2"""
R, Y, B = 'R', 'Y', 'B'


def r():
    s = input().split()
    cnt = int(s.pop(0))

    d = {
        'R': int(s[0]),
        'Y': int(s[2]),
        'B': int(s[4]),
        #'RY': int(s[1]),
        #'YB': int(s[3]),
        #'RB': int(s[5]),
    }

    mgen = ((v, k) for k, v in d.items())
    total = sum(d.values())
    m = max(mgen)
    if m[0] > total - m[0]:
        return 'IMPOSSIBLE'

    res = ''
    spaces = m[0]
    other = list(d.keys())
    other.remove(m[1])
    o1, o2 = other
    common = d[o1] + d[o2] - spaces
    oi1, oi2 = d[o1], d[o2]
    while total:
        total -= 1
        res += m[1]
        if common:
            common -= 1
            total -= 2
            res += o1
            res += o2
            oi1 -= 1
            oi2 -= 1
        elif oi1:
            total -= 1
            res += o1
            oi1 -= 1
        else:
            total -= 1
            res += o2
    return res



for case in range(1, int(input()) + 1):




    print('Case #{}: {}'.format(str(case), r()))
