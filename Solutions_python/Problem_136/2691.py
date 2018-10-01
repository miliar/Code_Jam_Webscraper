import sys


def get_farm_win(speed, C, X):
    return C/speed, X/speed


def compare_to_stop(farm, win, next_win):
        return win < farm + next_win


def calculate_time(C, F, X):
    total_time = 0.0
    speed = 2.0
    farm_time, win_time = get_farm_win(speed, C, X)
    while True:
        speed += F
        next_farm_time, next_win_time = get_farm_win(speed, C, X)
        if compare_to_stop(farm_time, win_time, next_win_time):
            total_time += win_time
            break
        else:
            total_time += farm_time
            farm_time, win_time = next_farm_time, next_win_time
    return total_time


def read_test_case():
    C, F, X = [float(no) for no in sys.stdin.readline().split()]
    return C, F, X


def format_answer(index, answer):
    output_line = "Case #%d: %.7f" % (index + 1, answer)
    return output_line


def display_results(answers):
    output_lines = []
    for index in range(len(answers)):
        output_line = format_answer(index, answers[index])
        output_lines.append(output_line)
    output = "\n".join(output_lines)
    with open("cookie_out.txt", "w") as f:
        print("%s" % output, file=f)


def main():
    line = sys.stdin.readline()
    test_cases = int(line.strip())
    answers = []
    for _ in range(test_cases):
        C, F, X = read_test_case()
        time = calculate_time(C, F, X)
        answers.append(time)
    display_results(answers)


if __name__ == "__main__":
    main()
