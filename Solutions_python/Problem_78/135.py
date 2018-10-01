#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import sys

index = 1
for line in [[int(y) for y in x.split()] for x in sys.stdin.readlines()][1:]:
    for D in range(1, min(line[0] + 1, 101)):
        d = line[1] * D / 100.0
        if int(d) == d:
            break
    else:
        print "Case #%d: Broken" % index
        index += 1
        continue
    for G in range(0, 100000):
        t = line[2] * (D + G) / 100.0
        if int(t) != t: continue
        if t >= d and t - d <= G:
            print "Case #%d: Possible" % index
            break
    else:
        print "Case #%d: Broken" % index
    index += 1

