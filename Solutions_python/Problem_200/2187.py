def brute(n):
    while True:
        digits = str(n)
        for i, ch in enumerate(digits[:-1]):
            if ch > digits[i+1]:
                break
        else:
            break
        n -= 1
    return n

def clever(n):
    if len(str(n)) == 1:
        return n

    n = list(map(int, list(str(n))))
    for i in range(len(n)-2, -1, -1):
        if n[i] > n[i+1]:
            for j in range(i+1, len(n)):
                n[j] = 9
            n[i] -= 1

    return int(''.join(map(str, n)))


for case in range(int(input())):
    n = int(input())
    #b = brute(n)
    c = clever(n)

    print('Case #%d: %d' % (case+1, c))
    #if b != c:
    #    print('%d: %d %d' % (n, b, c))
