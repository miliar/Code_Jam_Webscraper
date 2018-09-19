# Python 3

# q = {'1': 0, 'i': 1, 'j': 2, 'k': 3}
# qb = ['1', 'i', 'j', 'k', '-1', '-i', '-j', '-k']


def transform(a, b):
    """Takes string arguments and returns a string"""
    t = (a[0] == '-') + (b[0] == '-')
    l = a[-1]
    r = b[-1]
    if l == '1':
        ret = b[-1]
    elif r == '1':
        ret = a[-1]
    elif l == r:
        ret = '1'
        t += 1
    elif l == 'i':
        if r == 'j':
            ret = 'k'
        if r == 'k':
            ret = 'j'
            t += 1
    elif l == 'j':
        if r == 'k':
            ret = 'i'
        if r == 'i':
            ret = 'k'
            t += 1
    elif l == 'k':
        if r == 'i':
            ret = 'j'
        if r == 'j':
            ret = 'i'
            t += 1
    if t % 2:
        ret = '-' + ret
    return ret


def combine(l):
    ret = '1'
    for x in l:
        ret = transform(ret, x)
    return ret


t = int(input())
for tau in range(t):
    l, x = tuple(map(int, input().split()))
    s = list(input() * x)
    if combine(s) != '-1':
        print("Case #" + str(tau+1) + ": NO")
        continue
    while len(s) >= 3 and s[0] != 'i':
        s = [transform(s[0], s[1])] + s[2:]
    while len(s) >= 3 and s[-1] != 'k':
        s = s[:-2] + [transform(s[-2], s[-1])]
    if s[0] == 'i' and s[-1] == 'k':
        print("Case #" + str(tau+1) + ": YES")
    else:
        print("Case #" + str(tau+1) + ": NO")

