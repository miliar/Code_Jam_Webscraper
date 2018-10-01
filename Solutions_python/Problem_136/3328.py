#!/usr/bin/env python
"""
Problem B. Cookie Clicker
Solution:
  Recursive function that explores the routes of buying and not
  buying farms.
"""
import math

def minimum_cookie_time(farm_cost, farm_rate, target):
    """
    :farm_cost - cost to buy a farm
    :farm_rate - cookies per second per farm
    :target - target cookie value
    """
    cookie_rate = 2.0
    minimum_time = float('inf')
    max_number_of_farms = int(math.ceil(target / farm_cost))

    # There are up to max_number_farms configurations
    for farm_count in range(0, max(max_number_of_farms, 2)):
        modified_rate = cookie_rate
        time = 0.0
        # Determine rate to use for remainder
        for farm in range(1, farm_count + 1):
            time_till_farm = farm_cost / modified_rate
            time += time_till_farm
            modified_rate += farm_rate
        minimum_time = min(minimum_time, time + (target / modified_rate))

    return minimum_time


if __name__ == "__main__":
    time, num_of_cases = 0.0, int(raw_input())
    for i in range(1, num_of_cases + 1):
        farm_cost, farm_rate, target = raw_input().split()
        try:
            time = minimum_cookie_time(float(farm_cost), float(farm_rate), float(target))
        except RuntimeError as e:
            print "Case #{0}: Failed".format(i)
        else:
            print "Case #{0}: {1:.7f}".format(i, time)
