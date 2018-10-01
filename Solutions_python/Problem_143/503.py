import sys

# Round 1B - Problem B

i, result = 0, ""
lines = [l.rstrip() for l in sys.stdin.readlines()]
lines.pop(0)
while lines:
    i += 1
    a, b, k = [int(x) for x in lines.pop(0).split(" ")]
    n = 0
    for old in xrange(a):
        for new in xrange(b):
            if old & new < k:
                n += 1
    result = str(n)
    print "Case #%u: %s" % (i, result)

