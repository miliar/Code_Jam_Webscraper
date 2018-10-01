def tidy(n):
    while n:
        n2 = n // 10
        if n2 % 10 > n % 10:
            return False
        n = n2
    return True

less_tidy = list(range(1001))

for i in range(1001):
    if tidy(i):
        less_tidy[i] = i
    else:
        less_tidy[i] = less_tidy[i - 1]

T = int(input())

for i in range(1, T + 1):
    K = int(input())
    print('Case #{}: {}'.format(i, less_tidy[K]))

