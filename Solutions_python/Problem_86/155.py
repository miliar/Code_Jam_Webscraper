from collections import defaultdict
import time
from pprint import pprint

with file("C-small-0.in") as inp:
    with file("C-small-0.out", "w") as outp:
        full = int(inp.readline().strip())
        for casen in xrange(full):
            n, l, h = [int(x) for x in inp.readline().strip().split()]
            others = [int(x) for x in inp.readline().strip().split()]
            maxnote = -1
            maxharm = -1
            for note in xrange(l, h+1):
                harm = len(filter(lambda x: (x % note == 0) or (note % x == 0),
                                  others))
                if harm == n:
                    maxharm = harm
                    maxnote = note
                    break

            outp.write("Case #%s: " % (casen + 1))
            if maxnote < 0:
                outp.write("NO\n")
            else:
                outp.write("%s\n" % maxnote)

