def case():
    N = raw_input()
    candies = map(int, raw_input().split())
    xorsum = 0
    for candy in candies:
        xorsum ^= candy
    if xorsum != 0:
        return 'NO'
    else:
        return sum(candies)-min(candies)

T = int(raw_input())
for i in xrange(1, T+1):
    print 'Case #%i: %s' % (i, case())
