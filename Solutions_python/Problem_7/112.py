import sys

n = int(sys.stdin.readline())

def uc(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in uc(items[i+1:],n-1):
                yield [items[i]]+cc


for z in range(n):
    n, a, b, c, d, x, y, m = [int(x) for x in sys.stdin.readline().split()]
    l = [(x, y)]
    for i in range(1, n):
        x = (a * x + b) % m
        y = (c * y + d) % m
        l.append((x, y))
    result = 0
    for x in uc(l, 3):
        if (x[0][0] + x[1][0] + x[2][0]) % 3 == 0 and (x[0][1] + x[1][1] + x[2][1]) % 3 == 0:
            result += 1

    print "Case #%d: %d" %(z + 1, result)
