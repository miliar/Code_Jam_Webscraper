from sys import stdin

T = int(stdin.readline().rstrip())

for t in xrange(0, T):
    c, f, x = [float(n) for n in stdin.readline().rstrip().split(" ")]
    best = 1000000
    farms = 0
    curtime = 0
    while curtime < best:
        rate = 2 + farms*f
        tmp = curtime + x/rate
        if tmp < best:
            best = tmp
        curtime += c/rate
        farms += 1
    print "Case #%d: %.7f" % (t+1, best)
