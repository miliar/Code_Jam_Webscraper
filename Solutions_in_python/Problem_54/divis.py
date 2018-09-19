from fractions import gcd

inf = open("b.in", "r")
ouf = open("b.out", "w")

T = int(inf.readline())
for t in range(T):
    a = [int(i) for i in inf.readline().split()]
    n = a[0]
    del a[0]
    d = 1
    for i in range(n - 1):
        d = abs(a[i] - a[i + 1])
        if d > 0:
            break
    for i in range(n):
        for j in range(n):
            if a[i] > a[j]:
                d = gcd(d, a[i] - a[j])

    x = d - (a[0] % d)
    if x == d:
        x = 0
    print >> ouf, "Case #" + str(t + 1) + ": " + str(x)

inf.close()
ouf.close()
