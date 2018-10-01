import sys

def count(n):
    if n == 1:
        return 1
    return count(n - 1) * 2 + 1

f = open(sys.argv[1])
tst = int(f.readline())
for t in xrange(0, tst):
    ar = f.readline().split();
    n = long(ar[0])
    k = long(ar[1])

    cnt = count(n)

    res = "OFF"
    if k == cnt:
        res = "ON"
    if (k > cnt) and ((k - cnt) % (cnt + 1) == 0):
        res = "ON"

    print "Case #" + str(t + 1) + ":", res
    