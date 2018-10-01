def is_tidy(n):
    last = 0
    length = len(n)
    for j in range(0, length):
        if int(n[j]) >= last:
            last = int(n[j])
        else:
            return False
    return True


def tidy_numbers(case, n):
    for value in reversed(range(1, n + 1)):
        if is_tidy(str(value)):
            print("Case #{}: {}".format(case, value))
            return True
    return False


def run_program(filename):
    case = 0
    num_cases = 0
    for line in open(filename, 'r'):
        line = line.strip('\n')
        if case == 0:
            num_cases = line
        else:
            tidy_numbers(case, int(line))
        case += 1

run_program('B-small-attempt0.in')
