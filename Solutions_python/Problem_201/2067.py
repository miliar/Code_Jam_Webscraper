import sys

t = int(input())
lines = sys.stdin.read().splitlines()
i = 0
for line in lines:
    stalls = []
    i += 1
    n, m = [int(s) for s in line.split(' ')]
    stalls.append(n)
    if n != m:
        for k in range(0, m):
            stalls.sort()
            e = stalls.pop()
            if e % 2 == 0:
                l = (e / 2) - 1
                r = (e / 2)
            else:
                l = (e / 2)
                r = (e / 2)

            stalls.append(l)
            stalls.append(r)
    else:
        l = 0
        r = 0
    print("Case #{}: {} {}".format(i, max(l, r), min(l, r)))
