import sys
lines = open(sys.argv[1]).read().splitlines()
fp = open('OUTPUT.txt', 'w')

num_cases = int(lines.pop(0))
for case in range(num_cases):
    farm_cost, farm_rate, goal_cookies = [float(v) for v in lines.pop(0).split()]

    current_cookies = 0
    current_rate = 2.0
    current_time = 0

    while True:
        # time if wait for goal
        wait_time = goal_cookies / current_rate
        # time if get next farm
        farm_time = farm_cost / current_rate + goal_cookies / (current_rate + farm_rate)

        if farm_time < wait_time:
            # better to still invest in farms
            current_time += farm_cost / current_rate
            current_rate += farm_rate
        else:
            # better to wait
            current_time += wait_time
            break

    fp.write('Case #{}: {:.7f}\n'.format(case + 1, current_time))
fp.close()
