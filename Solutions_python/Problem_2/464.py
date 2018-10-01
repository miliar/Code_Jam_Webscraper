#!/usr/bin/env python

import operator
import re
import sys

line = sys.stdin.readline()
line = line.rstrip()

cases = int(line)

for case in range(0, cases):
    turnaround = int(sys.stdin.readline().rstrip())
    (abcount, bacount) = map(int, sys.stdin.readline().rstrip().split())

    times = {}

    def sched(count, departdesc, availdesc):
        for train in range(0, count):
            line = sys.stdin.readline().rstrip()
            m = re.search("(\d+):(\d+)\s+(\d+):(\d+)", line)
            if m:
                departtime = int(m.group(1))*60+int(m.group(2))
                arrivetime = int(m.group(3))*60+int(m.group(4))
                availtime = arrivetime+turnaround
                times.setdefault(departtime, []).append(departdesc)
                times.setdefault(availtime, []).append(availdesc)

    sched(abcount, "depart-a", "avail-b")
    sched(bacount, "depart-b", "avail-a")

    acount = 0
    bcount = 0

    aworst = acount
    bworst = bcount

    for time, desclist in sorted(times.iteritems(),key=operator.itemgetter(0)):
        for desc in desclist:
            if desc == "depart-a":
                acount -= 1
            elif desc == "depart-b":
                bcount -= 1
            elif desc == "avail-a":
                acount += 1
            elif desc == "avail-b":
                bcount += 1
        if acount < aworst:
            aworst = acount
        if bcount < bworst:
            bworst = bcount

    print "Case #%d: %d %d" % (case+1, -aworst, -bworst)
