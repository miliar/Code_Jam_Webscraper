from math import pi

t = int(input())
for i in range(1, t + 1):
    n, k = [int(e) for e in input().split(" ")]
    P = [[int(e) for e in input().split(" ")] for j in range(0, n)]
    P.sort(key=lambda l: l[0] * l[1])
    r = 0
    t = 0
    for j in range(0, k - 1):
        a = P.pop()
        r = max(r, a[0])
        t += a[0] * a[1] * 2 * pi
    v = t + r * r * pi
    M = v
    for u in P:
        r2 = max(r, u[0])
        M2 = t + r2 * r2 * pi + u[0] * u[1] * 2 * pi
        if M2 > M:
            M = M2

    print("Case #{}: {}".format(i, M))
