from sys import stdin

def riadok():
    return map(int, stdin.readline().split())
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for cas in range(int(stdin.readline())):
    n, l, h = riadok()
    a = riadok()
    mi = h + 1
    for v in range(l, h + 1):
        ok = True
        for x in a:
            if not (v % x == 0 or x % v == 0):
                ok = False
        if ok:
            mi = v
            break

    print "Case #%d:" % (cas + 1),
    if mi > h:
        print "NO"
    else:
        print mi
