#!/usr/bin/env python3


class Settings(object):

    def __init__(self, costs_farm, growth_increase_per_farm, end_amount):

        self.costs_farm = costs_farm
        self.growth_inc_farm = growth_increase_per_farm
        self.end_amount = end_amount


def run(instream):

    num_tests = int(instream.readline())

    for test_num in range(1, num_tests+1):
        costs_farm, growth_inc, end_amount = [float(num_str) for num_str in instream.readline().split(" ")]
        t = determine_time(costs_farm, growth_inc, end_amount)
        print(str.format("Case #{0}: {1:.7f}", test_num, t))


def determine_time(costs_farm, growth_increase_per_farm, end_amount):

    settings = Settings(costs_farm, growth_increase_per_farm, end_amount)

    cookies_curr = 0.0
    growth_rate = 2.0
    t_total = 0.0
    new_farm_useful = True

    while True:
        dt_end = time_till_end(cookies_curr, growth_rate, settings)
        if not new_farm_useful:
            t_total += dt_end
            break
        dt_farm = time_next_farm_available(cookies_curr, growth_rate, settings)
        if (dt_end <= dt_farm) or (dt_farm <= 0):
            t_total += dt_end
            break
        t_total += dt_farm
        cookies_curr += growth_rate * dt_farm
        if is_new_farm_useful(cookies_curr, growth_rate, settings):
            cookies_curr -= settings.costs_farm
            growth_rate += settings.growth_inc_farm
        else:
            new_farm_useful = False

    return t_total


def time_next_farm_available(cookies_curr, growth_rate, settings):

    return float(settings.costs_farm - cookies_curr) / growth_rate


def time_till_end(cookies_curr, growth_rate, settings):

    return float(settings.end_amount - cookies_curr) / growth_rate


def is_new_farm_useful(cookies_curr, growth_rate, settings):

    remaining_time_1 = float(settings.end_amount - cookies_curr) / growth_rate
    new_growth_rate = growth_rate + settings.growth_inc_farm
    remaining_time_2 = float(settings.end_amount - cookies_curr + settings.costs_farm) / new_growth_rate

    return remaining_time_2 < remaining_time_1


# ========== MAIN ==========

if __name__ == "__main__":

    import sys

    run(sys.stdin)


