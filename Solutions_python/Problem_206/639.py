t = int(input())

for tc in range(t):
    d, n = map(int, input().split())
    maxi = 0.0
    for i in range(n):
        k, s = map(int, input().split())
        h = (d - k) / s
        if h > maxi:
            maxi = h 
    print('Case #{}: {}'.format(tc + 1, d / maxi))