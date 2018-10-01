import math

ts = int(input())

for test in range(1, ts+1):
    n, k = map(int, input().split())
    cakes = []
    for i in range(n):
        r, h = map(int, input().split())
        cakes.append((r, h))

    ans = 0
    for bottom in range(len(cakes)):
        r, h = cakes[bottom]
        cur = math.pi * r ** 2 + 2 * math.pi * r * h
        cur_cakes = [cakes[i] for i in range(len(cakes)) if cakes[i][0] <= cakes[bottom][0] and i != bottom]
        cur_cakes.sort(key=lambda i: i[0] * i[1], reverse=True)

        if len(cur_cakes) >= k - 1:
            for i in range(k-1):
                r, h = cur_cakes[i]
                cur += 2 * math.pi * r * h
            ans = max(ans, cur)

    print('Case #{}: {}'.format(test, ans))
