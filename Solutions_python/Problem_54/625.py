def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for c in xrange(int(raw_input())):
    nums = set([int(n) for n in raw_input().split()[1:]])

    m = min(nums)
    T = reduce(gcd, [n-m for n in nums if n > m])

    print "Case #%d: %d" % (c+1, (T - (m % T)) % T)
