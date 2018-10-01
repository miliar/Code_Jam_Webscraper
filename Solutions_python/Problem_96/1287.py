T = int(raw_input())
for ii in xrange(T):
    nums = [int(x) for x in raw_input().split()]
    N, S, p = nums[0], nums[1], nums[2]
    ts = nums[3:]
    noSurp = len([x for x in ts if x >= 3 * p - 2])
    maybeSurp = len([x for x in ts if x >= 2 and (x == 3 * p - 4 or x == 3 * p - 3)])
    withSurp = min(maybeSurp, S)
    print 'Case #{case}: {maxP}'.format(
            case=ii + 1,
            maxP=withSurp + noSurp)

