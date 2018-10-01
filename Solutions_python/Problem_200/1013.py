T = int(input())
for I in range(1, T+1):
    n = input()
    i = len(n) - 2
    while i >= 0:
        e = n[i]
        p = n[i + 1]

        if e > p:
            n = n[:i] + str(int(e) - 1) + '9' * (len(n) - i - 1)
        p = e
        i -= 1

    print('Case #%s: %s' % (I, int(n)))
