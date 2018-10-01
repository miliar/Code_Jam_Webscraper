import sys, math
from sets import Set

input = sys.stdin
T = int(input.readline())
for t in xrange(T):
    count = 0
    f, l = (int(x) for x in input.readline().strip().split())
    dup = Set() 
    for n in xrange(f, l):
        dup.clear()
        numShift = int(math.log10(n))
        a = str(n)
        for s in xrange(numShift):
            a = a[len(a) - 1] + a[0:len(a)-1]
            if f <= n < int(a) <= l and int(a) not in dup:
                count += 1
                dup.add(int(a))
    print "Case #%d: %d" % (t + 1, count)
