from sys import stdin

for tc in xrange(1,1+int(stdin.readline())):
    (n,k) = tuple(int(z) for z in stdin.readline().split())
    # at most 4 different gapsizes exist
    gaps = {n:1}
    numCustomersLeft = k
    while True:
        maxgap = max(z for z in gaps)
        numgaps = gaps[maxgap]
        if numgaps >= numCustomersLeft:
            print "Case #%d: %d %d" % (tc, maxgap / 2, (maxgap - 1) / 2)
            break
        numCustomersLeft -= numgaps
        del gaps[maxgap]
        for z in [maxgap/2, (maxgap-1)/2]:
            if z not in gaps:
                gaps[z] = numgaps
            else:
                gaps[z] += numgaps
