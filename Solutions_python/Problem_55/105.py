#!/usr/bin/env python

t = raw_input()

for testcase_no in xrange(1, int(t)+1):
    l = [int(x) for x in raw_input().split()]

    R = l[0]
    k = l[1]
    N = l[2]

    g = [int(x) for x in raw_input().split()]

    ride_1 = dict()     #  next first queue, earned money

    for i in xrange(0, N):
        ptr = i
        weight = 0
        while weight + g[ptr] <= k:
            weight += g[ptr]
            ptr = (ptr + 1) % N
            if ptr == i: break

        ride_1[i] = (ptr, weight)

    def ride_double(ride_single):
        result = {}
        for i in xrange(0, N):
            ride_once, earned_1 = ride_single[i]
            ride_twice, earned_2 = ride_single[ride_once]

            result[i] = (ride_twice, earned_1 + earned_2)

        return result

    ride_mult = ride_1

    skip_count = 14

    skipper = 1<<skip_count
    for i in xrange(0, skip_count):
        ride_mult = ride_double(ride_mult)

    total_earned = 0
    ptr = 0

    while R >= skipper:
        next_ptr, earned = ride_mult[ptr]
        total_earned += earned
        ptr = next_ptr
        R -= skipper

    while R > 0:
        next_ptr, earned = ride_1[ptr]
        total_earned += earned
        ptr = next_ptr
        R -= 1
            
    print "Case #%d: %s" % (testcase_no, total_earned)

