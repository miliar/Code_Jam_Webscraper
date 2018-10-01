import sys

def potential_win_time(nfarms, c, f, x):
    current_rate = 2.0
    build_time = 0
    for i in range(nfarms):
        build_time += c / current_rate
        current_rate += f
    win_sec = (x / current_rate) + build_time
    return win_sec

def calculate(c, f, x):
    current_rate = 2.0
    win_sec = x / current_rate
    test_farms = 1
    test_more = True
    best_farm_win_sec = None
    while test_more:
        farm_win_sec = potential_win_time(test_farms, c, f, x)
        if best_farm_win_sec == None:
            best_farm_win_sec = farm_win_sec
        else:
            if farm_win_sec < best_farm_win_sec:
                best_farm_win_sec = farm_win_sec
            else:
                test_more = False
        test_farms += 1
    if best_farm_win_sec < win_sec:
        win_sec = best_farm_win_sec
    return win_sec

def read_data(file_name):
    test_cases = list()
    with open(file_name) as fl:
        t = int(fl.readline())
        for i in range(t):
            (c, f, x) = [float(i) for i in fl.readline().strip().split(' ')]
            test_cases.append((c, f, x))
    return test_cases

def main():
    file_name = sys.argv[1]
    data = read_data(file_name)
    case = 1
    with open('output.txt', 'w') as fl:
        for (c, f, x) in data:
            result = calculate(c, f, x)
            fl.write('Case #{0}: {1}\n'.format(case, result))
            case += 1

if __name__ == '__main__':
    main()