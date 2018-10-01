#!/usr/bin/python
# -*- coding: utf-8 -*-


def get_next_decide_point(rate, target, farm_cost, pts):
    time_required = (min(target, farm_cost) - pts) / rate
    return time_required


def decide(rate, target, farm_cost, rate_inc, pts):
    # time to achieve target as the current rate
    t1 = (target - pts) / rate

    # time to achieve target if we purchase the tractor
    t2 = (target - pts + farm_cost) / (rate + rate_inc)

    if t1 < t2:
        return None
    else:
        pts -= farm_cost    # buy the farm
        rate += rate_inc    # increment the rate
        return (pts, rate)


def solve(cipher):
    rate = 2    # the rate of getting cookies per second (initially)
    pts = 0.0   # the points
    time_elapsed = 0.0      # the time elapsed

    parts = cipher.strip().split()
    farm_cost = float(parts[0])     # the cost of a new farm
    rate_inc = float(parts[1])      # the increase in rate per second due to
                                    # new farm
    target = float(parts[2])

    # flag to check if we are done with the program
    done = False

    while not done:
        # go to the decide point
        time_to_next_decide_point = get_next_decide_point(rate, target,
                                                          farm_cost, pts)

        # add time required in going to the decide point to the elapsed time
        time_elapsed += time_to_next_decide_point
        pts += rate * time_to_next_decide_point

        if pts >= target:
            done = True
            continue

        # now decide
        decision = decide(rate, target, farm_cost, rate_inc, pts)

        if decision is None:
            done = True
        else:
            pts, rate = decision    # the new pts and rate

    # now when the control reaches here, just find how much more time is
    # required to reach the target
    time_elapsed += (target - pts)/rate

    return time_elapsed

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases + 1):
        cipher = raw_input()
        # print cipher
        print("Case #%i: %.7f" % (caseNr, solve(cipher)))
