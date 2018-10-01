import sys

FILE_NAME_PREFIX = 'B-large'


def minimum_time(cps, c, f, x):
    state = {
        'total_time': 0.0,
    }

    done = False
    while not done:
        time_without_buying_farm = x / cps
        time_buy_farm = c / cps
        next_time_without_buying_farm = x / (cps + f)

        if time_buy_farm + next_time_without_buying_farm < time_without_buying_farm:
            state['total_time'] += time_buy_farm
            cps += f
        else:
            state['total_time'] += time_without_buying_farm
            done = True

    return state['total_time']


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    input_file = open('in/' + FILE_NAME_PREFIX + '.in', 'r')
    output_file = open('out/' + FILE_NAME_PREFIX + '.out', 'w')
    test_case_nb = int(input_file.readline())

    for case in range(test_case_nb):
        c, f, x = [float(x) for x in input_file.readline().split()]
        res = minimum_time(2, c, f, x)

        res_str = '{0:.7f}'.format(res)
        output_file.write("Case #" + str(case + 1) + ": " + res_str + '\n')

    input_file.close()
    output_file.close()

