import sys

lines = open(sys.argv[1], "rb").read().splitlines()
res = ""

for t, line in enumerate(lines[1:]):
    n = int(line)
    dc = len(str(n))
    for i in xrange(dc - 1, 0, -1):
        dd = str(n)
        if dd[i] < max(dd[:i]):
            n -= int(dd[i:]) + 1
    res += "Case #%d: %d\n" % (t + 1, n)

open(sys.argv[2], "wb").write(res)
