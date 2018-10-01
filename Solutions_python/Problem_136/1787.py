#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


def n_farms(X, C, F):
    n_farms_lower_bound = X / C - 1 - 2 / F
    #print 'n_farms_lower_bound:', n_farms_lower_bound
    n_farms = max(int(n_farms_lower_bound), 0)
    return n_farms


MAX_X_SMALL = 2000
MAX_F_SMALL = 4
MAX_N_FARMS_SMALL = n_farms(MAX_X_SMALL, 1.0, MAX_F_SMALL)

MAX_X_LARGE = 100000
MAX_F_LARGE = 100
MAX_N_FARMS_LARGE = n_farms(MAX_X_LARGE, 1.0, MAX_F_LARGE)

#print '[small] max N farms:', MAX_N_FARMS_SMALL
#print '[large] max N farms:', MAX_N_FARMS_LARGE

N = MAX_N_FARMS_LARGE + 1

# pre-compute speeds and timings


def partial_sums(iterable, initializer=0):
    total = initializer
    for i in iterable:
        total += i
        yield total


def after_n_farms(C, F, X, n):
    speed = 2.0
    time = 0.0
    for __ in xrange(1, n):
        time += C / speed
        speed += F
    return speed, time


def solve1(C, F, X):
    print '+' * 80
    print C, F, X
    nF = n_farms(X, C, F)
    print 'n farms:', nF
    speed, time = after_n_farms(C, F, X, nF)
    print 'speed, time:', speed, time
    return time + X / speed
    #return 0.0
    #return 0.123456789


def IsApproximatelyEqual(x, y, epsilon):
    """Returns True iff y is within relative or absolute 'epsilon' of x.

    By default, 'epsilon' is 1e-6.
    """
    # Check absolute precision.
    if -epsilon <= x - y <= epsilon:
        return True

    # Is x or y too close to zero?
    if -epsilon <= x <= epsilon or -epsilon <= y <= epsilon:
        return False

    # Check relative precision.
    return (-epsilon <= (x - y) / x <= epsilon
            or -epsilon <= (x - y) / y <= epsilon)


epsilon = 1.0 / (10 ** 6)


def solve(C, F, X):
    speed = 2.0
    overall_time = 0.0
    while True:
        next_speed = speed + F
        time_now = X / speed
        time_to_next_farm = C / speed
        time_next = X / next_speed + time_to_next_farm
        if time_next < time_now:
            speed = next_speed
            overall_time_prev = overall_time
            overall_time += time_to_next_farm
            if IsApproximatelyEqual(overall_time_prev, overall_time, epsilon):
                break
        else:
            break
    return overall_time + X / speed


def numbers_from_line(d=' ', mapf=int):
    return [mapf(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


T = int(ifs.readline())
for t in range(1, T + 1):
    C, F, X = numbers_from_line(d=' ', mapf=float)
    a = solve(C, F, X)
    ofs.write('Case #%d: %s\n' % (t, a))
