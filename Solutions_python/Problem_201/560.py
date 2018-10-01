def answer(n, k):
    if k == 1:
        mid = (n + 1) // 2
        y = max(mid - 1, n - mid)
        z = min(mid - 1, n - mid)
        result = (y, z)
    else:
        # if n is odd and k is odd
        if n & 1 == 1 and k & 1 == 1:
            # last user on right
            result = answer(n // 2, k // 2)
        # if n is even and k is even
        elif n & 1 == 0 and k & 1 == 0:
            # last user on right
            result = answer(n // 2, k // 2)
        # if n is even and k is odd
        elif n & 1 == 0 and k & 1 == 1:
            # last user on left
            result = answer((n - 1) // 2, k // 2)
        # if n is odd and k is even
        elif n & 1 == 1 and k & 1 == 0:
            # last user on left
            result = answer(n // 2, k // 2)
    return result

t = input()
for i in range(1, t + 1):
    (n, k) = map(int, raw_input().split(' '))
    (y, z) = answer(n, k)
    print('Case #' + str(i) + ': ' + str(y) + ' ' + str(z))