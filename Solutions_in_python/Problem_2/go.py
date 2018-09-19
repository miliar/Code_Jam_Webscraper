#!/usr/bin/env python

import sys

def parse_time(t):
    hour, minute = [int(x) for x in t.split(":")]
    return hour * 60 + minute

def do_trial(f):
    turnaround_time = int(f.readline())
    a2b_count, b2a_count = [int(x) for x in f.readline().split()]
    #print turnaround_time, a2b_count, b2a_count

    events = []

    for i in xrange(a2b_count):
        leave_time, arrive_time = f.readline().split()
        leave_event = (parse_time(leave_time), 1, 0)
        events.append(leave_event)
        arrive_event = (parse_time(arrive_time)+turnaround_time, 0, 1)
        events.append(arrive_event)

    for i in xrange(b2a_count):
        leave_time, arrive_time = f.readline().split()
        leave_event = (parse_time(leave_time), 1, 1)
        events.append(leave_event)
        arrive_event = (parse_time(arrive_time)+turnaround_time, 0, 0)
        events.append(arrive_event)

    events.sort()

    max_a, max_b = 0, 0

    count_tuple = [0,0]

    for e in events:
        when, is_leaving, is_B = e
        if is_leaving:
            count_tuple[is_B] = count_tuple[is_B] + 1
        else:            
            count_tuple[is_B] = count_tuple[is_B] - 1
        #print "%02d:%02d : %s station %s (%d %d)" % (when/60, when%60, "leaving" if is_leaving else "arriving", "B" if is_B else "A", count_tuple[0], count_tuple[1])
        max_a = max(count_tuple[0], max_a)
        max_b = max(count_tuple[1], max_b)

    return max_a, max_b

f = sys.stdin
count = int(f.readline())
for i in xrange(count):
    a, b = do_trial(f)
    print "Case #%d: %d %d" % (i+1, a, b)
