input_file = "B-large.in"
output_file = "cookie_clicker_alpha.out"


def time_to_win(cookie_farm_cost, farm_production_rate, win_target):
    mapping = []  # maps the number of farms bought to win timing

    n_farms = 0
    cur_time = 0

    while True:
        cur_rate = cookie_rate(n_farms, farm_production_rate)

        win_timing = win_target / cur_rate + cur_time
        mapping.append(win_timing)

        if len(mapping) >= 2:
            if mapping[-1] > mapping[-2]:
                return mapping[-2]

        time_to_buy_farm = cookie_farm_cost / cur_rate
        n_farms += 1
        cur_time += time_to_buy_farm


def cookie_rate(n_farms, farm_production_rate):
    return 2 + n_farms * farm_production_rate


return_values = []
with open(input_file, 'r') as input:
    n_cases = int(input.readline())

    for i in range(n_cases):
        data = [float(i) for i in input.readline().split(' ')]
        cookie_farm_cost = data[0]
        farm_production_rate = data[1]
        win_target = data[2]

        return_values.append(time_to_win(cookie_farm_cost, farm_production_rate, win_target))


with open(output_file, 'w') as output:
    for i in range(len(return_values)):
        output.write("Case #{case_number}: {time_to_win}\n".format(
            case_number=i + 1,
            time_to_win=return_values[i])
        )


