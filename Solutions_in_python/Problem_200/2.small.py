cases = int(raw_input().split()[0])

def is_tidy(n):
    prev = n % 10
    n = n // 10

    while n != 0:
        curr = n % 10
        n = n // 10
        if curr > prev:
            return False
        prev = curr

    return True


for i in range(cases):
    n = int(raw_input())
    while not is_tidy(n):
        n -= 1
    print 'Case #%d: %d' % (i + 1, n)
