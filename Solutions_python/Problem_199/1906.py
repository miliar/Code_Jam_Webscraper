N = int(input())
for n in range(1, N+1):
    s, k = input().split()
    d = [c == '+' for c in s]
    k = int(k)
    i = 0
    imposs = False
    flips = 0
    while True:
        while i < len(d) and d[i]:
            i += 1
        if i >= len(d):
            break
        if i + k > len(d):
            imposs = True
            break
        flips += 1
        for j in range(i, i+k):
            d[j] = not d[j]
    if imposs:
        print('Case #{}: IMPOSSIBLE'.format(n))
    else:
        print('Case #{}: {}'.format(n, flips))
