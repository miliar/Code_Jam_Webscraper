#python 3

import argparse


def main():
    args = parse_arguments()
    parse_and_solve(args.input, args.output)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=argparse.FileType('r'),
                        nargs='?', default='input.txt', help='input file')
    parser.add_argument('output', type=argparse.FileType('w'),
                        nargs='?', default='output.txt', help='output file')

    return parser.parse_args()


def parse_and_solve(input, output):
    content = input.read()

    cases = parse_input(content)

    solutions = [solve(case) for case in cases]

    formatted_solutions = [format_solution(solution, i) for i, solution in enumerate(solutions)]
    joined_solutions = '\n'.join(formatted_solutions)

    output.write(joined_solutions)
    print(joined_solutions)


def parse_input(input):
    numbers = [x for x in input.split()]
    numbers.reverse()

    cases_count = int(numbers.pop())

    cases = []
    for i in range(cases_count):
        shy_max = int(numbers.pop())
        shyness = numbers.pop()
        shyness = [int(x) for x in list(shyness)]
        assert len(shyness) == (shy_max + 1)
        cases.append(shyness)

    assert(len(numbers) == 0)

    return cases


def solve(case):
    shyness = case
    standing = 0
    added = 0
    for shy_level, shyness_count in enumerate(shyness):
        if standing < shy_level:
            extra = shy_level - standing
            added += extra
            standing += extra
        standing += shyness_count
    return added


def format_solution(solution, index):
    format_ = 'Case #%d: %d'
    return format_ % (index + 1, solution)

if __name__ == '__main__':
    main()
