fn = 'B-large'
f = open('%s.in' % fn, 'r')
o = open('%s.out' % fn, 'w')

tests = int(f.readline().strip())

for test in xrange(tests):
    totals = map(int, f.readline().strip().split(' '))
    gcount = totals.pop(0)
    surprises = totals.pop(0)
    check = totals.pop(0)
    finals = []
    result = 0
    possible = 0
    for s in totals:
        scores = [s / 3, s / 3, s / 3]
        for i in xrange(0,s % 3):
            scores[i] += 1
        sum = scores[0]+scores[1]+scores[2]

        if max(scores) >= check:
            result += 1
        elif s%3 in (0,2) and (check - max(scores)) <= 1 and sum >= 2:
            possible += 1
    result += min([surprises, possible])
    s = "Case #%d: %d\n" % (test+1, result)
    print s
    o.write(s)
