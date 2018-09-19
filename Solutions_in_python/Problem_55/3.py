#!python

import sys

fh = open(sys.argv[1], 'r')
n_cases = int(fh.readline())

for i in xrange(0, n_cases):
    (r, k, n) = map(lambda x: int(x), fh.readline().split())
    ns = map(lambda x: int(x), fh.readline().split())
    assert(len(ns) == n)
#    print "%d %d %d %s" % (r, k, n, str(ns))

    total_euros = 0
    for ride in xrange(0, r):
        n_people = 0
        curr = 0
        while curr < n and n_people + ns[curr] <= k:
            n_people += ns[curr]
            curr += 1
        total_euros += n_people
        ns = ns[curr:] + ns[:curr]

    print "Case #%d: %d" % (i+1, total_euros)
            
