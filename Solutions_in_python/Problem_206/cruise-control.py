import fileinput


# Solve problem

def add_interval(intervals, interval_size, times):
    if interval_size in intervals:
        intervals[interval_size] += times
    else:
        intervals[interval_size] = times


def remove_interval(intervals, interval_size, times):
    intervals[interval_size] -= times
    if intervals[interval_size] is 0:
        del intervals[interval_size]


def get_biggest_interval(intervals):
    return max(intervals.keys())


def lower_half(number):
    return int(number // 2)


def upper_half(number):
    return number - lower_half(number)


def solve_problem(d, n, horses):
    times_of_arrival = []
    for (k, s) in horses:
        time_of_arrival = (d-k) / s
        times_of_arrival.append(time_of_arrival)
    return d / max(times_of_arrival)


# Utils

def solve_case(d, n, horses, case_number):
    print("Case #" + str(case_number) + ": " + str(solve_problem(d, n, horses)))


# Main script

def main():
    case = 1
    is_new_problem = True
    d = 0
    n = 1
    horses = []
    for index, line in enumerate(fileinput.input()):
        if index is 0:
            continue

        if not is_new_problem:
            [k, s] = line.split(' ')
            horses.append((int(k), int(s)))

        if len(horses) is n:
            solve_case(d, n, horses, case)
            case += 1
            is_new_problem = True
            d = 0
            n = 1
            horses = []
            continue

        if is_new_problem:
            horses = []
            line = line.strip()
            [parsed_d, parsed_n] = line.split(' ')
            d = int(parsed_d)
            n = int(parsed_n)
            is_new_problem = False

if __name__ == "__main__":
    main()
