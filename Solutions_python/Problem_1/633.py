#!/usr/bin/python

import sys

def universe(queries, engines):
    if len(queries) == 0:
        return 0
    indices = []
    for engine in engines:
        try:
            indices.append(queries.index(engine))
        except ValueError:
            return 0
    switch = universe(queries[max(indices):], engines)

    return switch + 1

f = open("A-small-attempt4.in","rb")
casos = int(f.readline())
for i in xrange(casos):
    engines = []
    queries = []
    engs = int(f.readline())
    for j in range(engs):
        engines.append(f.readline())
    ques = int(f.readline())
    if ques == 0:
        print "Case #%d: 0" % (int(i)+1)
        continue
    for k in range(ques):
        queries.append(f.readline())  

    switchs = universe(queries, engines)
    
    print "Case #%d: %d" % (int(i)+1, switchs)
                


        
