import sys
import operator
f = sys.stdin

t = int(f.next())
for case in xrange(1, t+1):
    n = int(f.next())
    l = map(int, f.next().split())
    result = len(filter(lambda (x, y): x+1 != y, enumerate(l)))
    print "Case #%d: %d.000000" % (case, result)
