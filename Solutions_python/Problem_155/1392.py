def print_result(i, result):
    print 'Case #%s: %s' % (i+1, result)

T = input()
for i in range(T):
    Smax, digits = raw_input().split(' ')

    current = 0
    needed = 0
    for S, c in enumerate(digits):
        N = ord(c) - ord('0')
        if current < S and N != 0:
            needed  += S - current
            current += N + needed
        else:
            current += N
    print_result(i, needed)
