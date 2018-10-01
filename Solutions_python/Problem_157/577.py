from sys import stdin

def third(i, j):
    for c in ['i', 'j', 'k']:
        if c not in [i, j]:
            return c

def mul(s, x):
    s = s * (x % 12 + (0 if x < 12 else 12))
    sign = 1
    cur = None
    STEP = 0
    for c in s:
        if cur is None:
            cur = c
        elif cur == c:
            sign *= -1
            cur = None
        else:
            if (cur, c) in [('i', 'k'), ('j', 'i'), ('k', 'j')]:
                sign *= -1
            cur = third(c, cur)

        if (cur, sign) == ('i', 1) and STEP == 0:
            STEP = 1
        elif (cur, sign) == ('k', 1) and STEP == 1:
            STEP = 2

    if cur is None:
        cur = '1'
    if sign == -1:
        cur = '-' + cur
    return (cur, STEP)

def solve(tc):
    l, x = map(int, stdin.readline().split())
    s = stdin.readline().strip()
    if mul('ijk', 1)[0] == mul(s, x)[0] and mul(s, x)[1] == 2:
        result = 'YES'
    else:
        result = 'NO'
    print 'Case #%d: %s' % (tc, result)


d = int(stdin.readline())
for i in range(d):
    solve(i + 1)


