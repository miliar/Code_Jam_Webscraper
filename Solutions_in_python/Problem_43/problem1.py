cases = int(raw_input())

for case in xrange(cases):
    digits = {}
    i = raw_input()

    digits[i[0]] = 1
    num = 0
    for thing in i[1:]:
        if thing not in digits:
            digits[thing] = num
            num += 1
            if num == 1:
                num = 2

    min = {}

    newnum = ''
    for thing in i:
        newnum += str(digits[thing])

    if len(digits) == 1:
        newnum = int(newnum, 2)
    else:
        newnum = int(newnum, len(digits))

    print 'Case #%d: %d' % (case + 1, newnum)
