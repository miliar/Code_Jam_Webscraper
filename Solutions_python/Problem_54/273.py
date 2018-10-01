import sys

def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

def read_int():
    return [int(e) for e in sys.stdin.readline().split()]

C = read_int()[0]

for cases in xrange(1, C+1):
    
    ii = read_int()
    N, t = ii[0], ii[1:]

    g = reduce(gcd, t)

    d, diff = [x/g for x in t], []

    for a in d:
        for b in d:
            if a != b:
                diff.append(abs(a-b))

    r = reduce(gcd, diff)
    if r != 1:
        res = g * (r - d[0] % r)
    else:
        res = 0

    print "Case #%d: %d" % (cases, res)
