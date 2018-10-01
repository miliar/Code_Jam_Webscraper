t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())
    decimal = list()
    while n > 0:
        decimal = [n % 10] + decimal
        n /= 10
    j = len(decimal)-1
    while not decimal == sorted(decimal):
        decimal[j] = 9
        j -= 1
        decimal[j] -= 1
    j = len(decimal)-1
    for d in decimal:
        n += d*(10**j)
        j -= 1
    print "Case #{}: {}".format(i, n)

