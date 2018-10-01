T = int(input())

for t in range(T):
    N, s = input().split()
    N, s = int(N), list(map(int, s))
    a = 0
    n = 0
    for i in range(N + 1):
        d = max(0, i - n)
        a += d
        n += s[i] + d
    print('Case #{0}: {1}'.format(t + 1, a))
