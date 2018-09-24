#!/usr/bin/python2.5

for case in range(input()):
    engines = set()
    for i in range(input()):
        engines.add(raw_input())
    s = 0
    t = engines.copy()
    for k in range(input()):
        q = raw_input()
        t.discard(q)
        if not len(t):
            s = s + 1
            t = engines.copy()
            t.discard(q)

    print "Case #%s: %s" % ((case + 1), s)

