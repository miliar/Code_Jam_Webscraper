def tidy(n):
    prev = '0'
    for d in str(n):
        if d < prev:
            return False
        prev = d
    return True

for t in range(int(input())):
    n = int(input())
    a = 1
    while True:
        if tidy(n):
            break
        d = (n // a) % 10
        if d != 9:
            n -= (d + 1) * a
        a *= 10

    print('Case #%d: %d' % (t+1, n))
