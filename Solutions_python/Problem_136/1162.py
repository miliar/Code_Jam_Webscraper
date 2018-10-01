import sys

f = open(sys.argv[1])
T = int(f.readline())
for t in xrange(1,T+1):
    C, F, X = map(float, f.readline().strip().split())
    rt = (X - C) * F / C
    time, rate = 0, 2
    while rate < rt:
        time += C / rate
        rate += F
    time += X / rate
    print "Case #{0}: {1}".format(t, time)
