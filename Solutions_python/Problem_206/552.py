t = int(input())

for case in range(1, t + 1):
    d, n = map(int, input().split())
    ks, ss = [], []
    for _ in range(n):
        k, s = map(int, input().split())
        ks += [k]
        ss += [s]

    slowest = 0
    for k, s in zip(reversed(ks), reversed(ss)):
        t = (d - k) / s
        slowest = max(t, slowest)
    print('Case #{}: {}'.format(case, d / slowest))
