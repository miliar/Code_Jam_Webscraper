#!/usr/bin/python

import sys
import math

def factorial( n ):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


def nchoosek( n, k ):
    #return factorial(n)/(factorial(k)*factorial(n-k))
    answer = 1
    for i in range(1,k+1):
        answer *= (n - (k - i))
        answer /= i
    return answer


f = open( sys.argv[1] )

num_cases = int(f.readline().split()[0])

for i in range(num_cases):
    line = f.readline().strip()
    if len(line) <= 0:
        continue
    [farm_cost, extra_rate, win_amount] = [float(x) for x in line.split()]

    # If we're going to buy one, it makes sense to buy it ASAP
    # If we ever choose not to buy one, we're not buying any after that

    # How do we decide whether to buy one?
    # We want to know whether time_with_buying < time_without_buying
    # time_with_buying is (win_amount - current_oookies + farm_cost)
    #                    /(current_rate + extra_rate)
    # time without buying is (win_amount - current_cookies)/current_rate
    # we can multiply by denominators to get 
    # current_rate*(win_amount - current_cookies + farm_cost) <
    # (current_rate+extra_rate)*win_amount - current_cookies)
    # We can subtract some stuff from both sides to get
    # current_rate*farm_cost < extra_rate*win_amount - 
    #                                extra_rate*current_cookies

    # When do we need to make decisions?
    # When you're making the decision, current_cookies will always be farm_cost
    # So the only variable is current_rate
    # so you stop buying when current_rate is such that 
    # current_rate*farm_cost >= extra_rate*(win_amount - current_cookies)
    threshold_rate = extra_rate*(win_amount - farm_cost)/farm_cost
    #print extra_rate
    #print win_amount - farm_cost
    #print farm_cost
    #print threshold_rate

    # So you will have bought how many farms?
    # (threshold_rate - 2)/extra_rate
    # But we need to add 1
    # WHAT IF IT'S EXACT?
    #final_num_farms = int(((threshold_rate - 2)/extra_rate)) + 1
    final_num_farms = int(math.ceil((threshold_rate - 2)/extra_rate))
    if final_num_farms < 0:
        final_num_farms = 0
    #print final_num_farms

    # When you bought your last farm, you ended up with 0
    # total time is time_to_buy_first_farm + time_to_buy_second +....
    # + time_to_buy_last_farm + time_to_win
    # That's farm_cost/2 + farm_cost/(2 + extra_rate) + farm_cost/(2 + 2*extra_rate) + ... + time_to_win
    # IS THIS LOOP FAST ENOUGH OR DO WE NEED TO USE MATH TO GET OUT OF IT?
    farm_building_time = 0
    for j in range(final_num_farms):
        farm_building_time += 1/(2 + j*extra_rate)
    farm_building_time *= farm_cost
    #print farm_building_time

    final_rate = 2 + final_num_farms*extra_rate
    time_to_win = win_amount/final_rate
    #print time_to_win

    total_time = farm_building_time + time_to_win
    #print total_time

    print "Case #" + str(i+1) + ":", total_time

