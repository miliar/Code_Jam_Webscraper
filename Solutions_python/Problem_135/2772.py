rl = raw_input

cases = int(rl())
for cc in xrange(cases):
    r1 = int(rl())
    first = set(map(int, [rl() for i in xrange(4)][r1-1].split()))
    r2 = int(rl())
    second = set(map(int, [rl() for i in xrange(4)][r2-1].split()))
    cands = first & second
    if len(cands) > 1:
        sol = 'Bad magician!'
    elif len(cands) == 0:
        sol = 'Volunteer cheated!'
    else:
        sol = '%d' % list(cands)[0]
    print 'Case #%d: %s' % (cc+1, sol)
