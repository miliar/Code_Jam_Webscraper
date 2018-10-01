import numpy as np

def cmp0(x, y):
    if x == y:
        return False
    if x == 'r' and y == 'o':
        return False
    if x == 'y' and y == 'o':
        return False
    if x == 'y' and y == 'g':
        return False
    if x == 'b' and y == 'g':
        return False
    if x == 'r' and y == 'v':
        return False
    if x == 'b' and y == 'v':
        return False
    return True

def cmp(x, y):
    return cmp0(x, y) and cmp0(y, x)

print(cmp('r', 'o'))
print(cmp('o', 'r'))
print(cmp('v', 'b'))
print(cmp('v', 'y'))

from operator import itemgetter

def check(l):
    if not cmp(l[0], l[-1]):
        return False
    for i in range(len(l) - 1):
        if not cmp(l[i], l[i+1]):
            return False
    return True

def solve(l):
    r, o, y, g, b, v = l
    n = r + o + y + g + b + v
    h = {}
    h['r'] = r
    h['o'] = o
    h['y'] = y
    h['g'] = g
    h['b'] = b
    h['v'] = v
    l = []
    filled = {}
    filled['r'] = 0
    filled['o'] = 0
    filled['y'] = 0
    filled['g'] = 0
    filled['b'] = 0
    filled['v'] = 0

    def f(x):
        h1 = {}
        for k, v in h.items():
            if v > 0 and (x is None or cmp(x, k)):
                if k in ['v', 'o', 'g']:
                    v *= 2
                if len(l) < n / 2:
                    v -= filled[k] / 10000000000
                else:
                    v += filled[k] / 10000000000
                h1[k] = v
        if len(h1) == 0:
            return None
        k = max(h1.items(), key=itemgetter(1))[0]
        return k

    while any(x > 0 for x in h.values()):
        k = f(l[-1] if len(l) > 0 else None)
        if k is None:
            return 'IMPOSSIBLE'
        l.append(k)
        filled[k] += 1
        h[k] -= 1
    if check(l):
        return (''.join(l)).upper()
    else:
        return 'IMPOSSIBLE'

with open('in.txt') as f_in:
    with open('out.txt', 'w') as f_out:
        next(f_in)
        for i, line in enumerate(f_in):
            l = line[:-1].split()
            l = [int(x) for x in l[1:]]
            s = solve(l)
            out = 'Case #%s: %s\n' %(i+1, s)
            print(out)
            f_out.write(out)
