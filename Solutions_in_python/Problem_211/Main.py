from decimal import Decimal

Tn = input()
for Tc in range(1, Tn + 1):
    n,k = map(int, raw_input().split())
    u = Decimal(raw_input().strip())
    a = map(Decimal, raw_input().split())
    delta = Decimal('0.0001')

    # print n, k, u, a, delta
    while u > 0:
        mini = 0
        for i in xrange(1, n):
            if a[i] < a[mini]:
                mini = i
        u -= delta
        a[mini] += delta

    ans = Decimal(1)
    for d in a:
        ans *= d

    print 'Case %d:'% Tc,
    print '%.10f' % ans