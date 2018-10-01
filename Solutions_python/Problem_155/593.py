for tc in range(1, int(raw_input())+1):
    standing = 0
    required = 0
    shyness = 0
    for digit in map(int, raw_input().split()[1]):
        if shyness > standing:
            required += shyness-standing
            standing += shyness-standing
        standing += digit
        shyness += 1
    print 'Case #%d: %d' % (tc, required)