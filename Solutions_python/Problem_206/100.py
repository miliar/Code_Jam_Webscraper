#!/usr/bin/env python


num_tests = input()

for test_no in xrange(1, num_tests + 1):
    dest, n_horses = map(int, raw_input().split())
    latest_arrival = 0
    for horse_no in xrange(n_horses):
        x, s = map(int, raw_input().split())
        dist = dest - x
        if dist <= 0:
            continue
        arrival_time = 1.0 * dist / s
        latest_arrival = max(latest_arrival, arrival_time)
    speed = 1.0 * dest / latest_arrival
    print 'Case #%d: %.6f' % (test_no, speed)
