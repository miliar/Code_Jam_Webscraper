import sys
read = lambda t=int: list(map(t,sys.stdin.readline().split()))
array = lambda *ds: [array(*ds[1:]) for _ in range(ds[0])] if ds else 0

T, = read()
for t in range(T):
    N, X = read()
    xs = read()

    bigs = sorted(X-x for x in xs if x > X//2)
    smalls = sorted(x for x in xs if x <= X//2)

    i, j = 0, 0
    while i != len(smalls) and j != len(bigs):
        if smalls[i] <= bigs[j]:
            i, j = i+1, j+1
        elif smalls[i] > bigs[j]:
            j += 1

    res = (len(smalls)-i+1)//2 + len(bigs)
    print('Case #{}:'.format(t+1), res)
