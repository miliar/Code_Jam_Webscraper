from operator import add, sub, mul, div
from itertools import imap, ifilter, izip, repeat, count, chain

cases = int(raw_input())
for case in xrange(cases):
    length = int(raw_input())
    a = map(int, raw_input().split())
    b = map(int, raw_input().split())
    rev = lambda a, b: cmp(b, a)
    print "Case #%i: %s" % (case + 1, sum(imap(mul, sorted(a), sorted(b, rev))))
