T = int(input())

for t in range(1, T+1):
    d, n = map(int, input().split())
    maxt = 0
    for _ in range(n):
        dd, v = map(int, input().split())
        maxt = max(maxt, (d-dd)/v)

    print("Case #%d: %f" % (t, d/maxt))
