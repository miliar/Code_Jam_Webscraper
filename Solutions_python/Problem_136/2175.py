def run():
    f = open('B-large.in')
    number_of_testcase = f.readline()

    for test_case in range(1, int(number_of_testcase)+1):
        game_param = f.readline().split(' ')

        game_param = map(lambda x: float(x), game_param)

        last_best_time = game_param[2] / 2.0

        current_production_rate = 2.0
        accum = 0.0
        while True:
            new_time = calculated_time(game_param[0], game_param[1], game_param[2], current_production_rate, accum)
            if new_time > last_best_time:
                break
            else:
                last_best_time = new_time
            accum += game_param[0] / current_production_rate
            current_production_rate += game_param[1]

        print '%s%s%s%.7f' % ('Case #', test_case, ': ', last_best_time)

    f.close()


def calculated_time(farm_cost, extra_production_rate, target_cookie, current_production_rate, accum):
    time_for_a_form = farm_cost / current_production_rate
    return float(target_cookie) / float(current_production_rate + extra_production_rate) + float(time_for_a_form) + float(accum)


if __name__ == '__main__':
    run()