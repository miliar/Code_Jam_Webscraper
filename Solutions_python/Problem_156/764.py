import math

def max_i(arr):
    best = 0
    for i in range(1, len(arr)):
        if arr[best] < arr[i]:
            best = i
    return best

def solve(p):
    total = sum(p)
    best = max(p)
    for q in range(1, total - len(p) + 1):
        m = q + len(p)
        splits = [1 for i in range(len(p))]
        c = [int(math.ceil(pi / split)) for pi, split in zip(p, splits)]
        for qi in range(q):
            x = max_i(c)
            splits[x] += 1
            c[x] = int(math.ceil(p[x] / splits[x]))
        time = q + max(c)
        if time < best:
            best = time

    return best

cases = int(input())
for t in range(1, cases+1):
    input()
    arr = [int(s) for s in input().split(' ')]
    res = solve(arr)
    print('Case #%d: %d' % (t, res))
