import sys

def initialize(fname):
    # open
    with open(fname) as f:
        lines = f.readlines()

    # clean
    for i, line in enumerate(lines):
        lines[i] = [int(n) for n in line.split()]
        if len(lines[i]) == 1:
            lines[i] = lines[i][0]

    # parse
    NUM_TESTS = lines.pop(0)
    tests = []

    for test in range(NUM_TESTS):
        first_round = lines.pop(0), [lines.pop(0) for _ in range(4)]
        second_round = lines.pop(0), [lines.pop(0) for _ in range(4)]
        tests.append((first_round, second_round))

    return tests

def finalize(answers):
    for test_num, answer in enumerate(answers, 1):
        print('Case #{}: {}'.format(test_num, answer))

def process_test(test):
    first, second = test
    first_answer, first_board = first
    second_answer, second_board = second
    # actual business
    first_result = set(first_board[first_answer - 1])
    second_result = set(second_board[second_answer - 1])
    intersection = first_result & second_result
    if len(intersection) == 1:
        return list(intersection)[0]
    elif len(intersection) > 1:
        return 'Bad magician!'
    else:
        return 'Volunteer cheated!'

def main(fname='magic_trick.input'):
    tests = initialize(fname)
    answers = [process_test(t) for t in tests]
    finalize(answers)

if __name__ == '__main__':
    fname = sys.argv[1]
    main(fname)
