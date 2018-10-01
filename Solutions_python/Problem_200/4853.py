def is_tidy(n):
    prev = 10
    while n > 0:
        digit = n % 10
        if digit > prev:
            return False
        prev = digit
        n //= 10
    return True

test = int(input(''))
case = 1
for _ in range(test):
    n = int(input(''))
    while not is_tidy(n):
        n -= 1
    print('Case #{}: {}'.format(case, n))
    case += 1
