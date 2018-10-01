def swaps(nb):
    n = 0
    i = nb
    while i > 0:
        n += 1
        i /= 10

    for i in xrange(n-1):
        a = nb%10
        nb /= 10
        nb += a*10**(n-1)
        yield nb

def recycling(a,b):
    nb = 0
    for n in xrange(a,b):
        s = []
        for m in set(swaps(n)):
            if m > n and m <= b:
                nb += 1

    return nb


nb = int(raw_input())
pairs = [tuple(map(int,raw_input().split())) for _ in xrange(nb)]
for i in xrange(nb):
    print "Case #%s: %s" %(i+1, recycling(*pairs[i]))
