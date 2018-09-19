from __future__ import with_statement
from sys import argv

with open(argv[1]) as filein:
    inp = filein.read().splitlines()

nbcase = int(inp.pop(0))

for case in range(nbcase):
    nbengine = int(inp.pop(0))
    engines = inp[:nbengine]
    del inp[:nbengine]
    nbquery = int(inp.pop(0))
    queries = inp[:nbquery]
    del inp[:nbquery]

    switch = 0
    tmpengines = engines[:]
    for query in queries:
        if query in tmpengines:
            tmpengines.remove(query)
            if not tmpengines:
                switch += 1
                tmpengines = engines[:]
                tmpengines.remove(query)

    print "Case #%d: %d" % (case+1, switch)