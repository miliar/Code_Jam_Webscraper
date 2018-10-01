import sys

input = sys.stdin

T=int(input.readline())
for i in xrange(1,T+1):
    data = input.readline()
    data = input.readline()
    data = map(int, data.split())

    # + is ^
    if reduce(lambda x, y: x ^ y, data) != 0:
        res = 'NO'
    else:
        data.sort()
        res = sum(data[1:])
    print "Case #%s: %s" % (i, res)
