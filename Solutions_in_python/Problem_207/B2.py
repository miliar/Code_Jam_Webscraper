import sys
sys.setrecursionlimit(10**6)

d = set()

OK = {
    'R': set(['Y', 'B', 'G']),
    'Y': set(['R', 'B', 'V']),
    'B': set(['R', 'Y', 'O']),
    'O': set(['B']),
    'G': set(['R']),
    'V': set(['Y']),
}

N1 = {
    'R': ['Y', 'B'],
    'Y': ['R', 'B'],
    'B': ['R', 'Y'],
}

N2 = {
    'O': 'B',
    'G': 'R',
    'V': 'Y',
}

N2r = {
    'B': 'O',
    'R': 'G',
    'Y': 'V',
}

def solve2(res, left):
    first, last = res[0], res[-1]

    N = sum(left.values())
    if N == 0:
        return res if last in OK[first] else None

    ns = N1[last]
    x = None
    if left[ns[0]] > left[ns[1]]:
        x = ns[0]
    elif left[ns[1]] > left[ns[0]]:
        x = ns[1]
    elif left[ns[0]] > 0:
        x = ns[0]

    if x:
        n = x
        if left[n] > 0:
            res.append(n)
            left[n] -= 1
            r = solve2(res, left)
            if r: return r
            left[n] += 1
            res.pop()
        else:
            return None
    return None

def solve():
    global d
    N, R, O, Y, G, B, V = (int(x) for x in input().split())
    left = {'R': R, 'O': O, 'Y': Y, 'G': G, 'B': B, 'V': V}
    for x in ('R', 'Y', 'B'):
        if left[x] > 0:
            left[x] -= 1
            res = solve2([x], left)
            if res: return ''.join(res)
            left[x] += 1

    return "IMPOSSIBLE"

T = int(input())
for t in range(1, T + 1):
    print ("Case #%d: %s" % (t, solve()))
