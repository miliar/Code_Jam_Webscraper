from sys import argv


def cookies_per_second(farms):
    return 2.0 + sum([x[0] for x in farms])

def total_farm_output(time, farm):
    return farm[0] * (time - farm[1])

def total_cookies(time, farms):
    return (2 * time) + sum([total_farm_output(time, f) for f in farms])

def time_to_get_cookies(n, farms):
    return float(n) / cookies_per_second(farms)

def time_until_next_farm(cookies, cost, farms):
    return time_to_get_cookies(cost - cookies, farms)



def run_test(cost, farmout, win):
    cookies = 0
    farms = []
    time = 0

    while cookies < win:
        prod = cookies_per_second(farms)

        farm_until = time_until_next_farm(cookies, cost, farms)
        farm_t = time + farm_until
        new_farm = (farmout, farm_t)

        win_until = time_to_get_cookies(win - cookies, farms)
        win_t = time + win_until

        win_until_with_farm = farm_until + time_to_get_cookies(win, farms + [new_farm])

        if (win_until < farm_until) or (win_until < win_until_with_farm):
            return win_t
        else:
            farms.append(new_farm)
            time = farm_t
        
        

def response(n, result):
    return 'Case #{}: {}'.format(n+1, result)


if __name__ == '__main__':
    INPUT = open(argv[1] if len(argv) > 1 else "/tmp/shiner")
    lines = [x.strip() for x in INPUT.readlines()]

    num_tests = lines.pop(0)

    for i,line in enumerate(lines):
        print response(i, run_test(*[float(x) for x in line.split(' ')]))

