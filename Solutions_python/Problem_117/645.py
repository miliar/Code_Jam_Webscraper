"""
Solve Lawnmower problem.
"""

import argparse

def main():
    args = parse_argumnets()
    solve(args.input, args.output)

def parse_argumnets():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', default='input.txt')
    parser.add_argument('--output', default='output.txt')
    return parser.parse_args()

def solve(input_file_name, output_file_name):
    input = open(input_file_name, 'r').read()
    cases = parse_input(input)

    solutions = [solve_problem(case) for case in cases]

    formatted_solution = format_solutions(solutions)

    open(output_file_name, 'w').write(formatted_solution)

def parse_input(input):
    lines = [l.strip() for l in  input.splitlines() if l.strip() != '']
    current_line = 0

    cases_count = int(lines[current_line])
    current_line += 1

    cases = []
    for i in range(cases_count):
        raws_count, columns_count = parse_ints(lines[current_line])
        current_line += 1

        raws = [parse_ints(line) for line in lines[current_line : current_line + raws_count]]
        current_line += raws_count

        assert all(len(raw) == columns_count for raw in raws)

        cases.append(raws)

    return cases

def parse_ints(string):
    return [int(s) for s in string.split()]

def solve_problem(raws):
    columns = transpose(raws)

    raw_maximums = [max(raw) for raw in raws]
    columns_maximums = [max(column) for column in columns]

    for raw_index, raw in enumerate(raws):
        for column_index, patch_height in enumerate(raw):
            raw_maximum = raw_maximums[raw_index]
            column_maximum = columns_maximums[column_index]
            if patch_height < raw_maximum and patch_height < column_maximum:
                return False

    return True

def transpose(x):
    return zip(*x)

def format_solutions(solutions):
    format = 'Case #%d: %s'
    return '\n'.join(format % (i + 1, 'YES' if s else 'NO') for i, s in enumerate(solutions))

if __name__ == '__main__':
    main()
