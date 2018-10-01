#! /usr/bin/env python

import sys

ARRANGEMENT_SIZE   = 4
MULTIPLE_SOLUTIONS = "Bad magician!"
NO_SOLUTION        = "Volunteer cheated!"

def solve_magic_trick(first_row, first_arrangement, second_row,
        second_arrangement):
    first_index = first_row - 1
    second_index = second_row - 1

    first_row = first_arrangement[first_index]
    second_row = second_arrangement[second_index]
    set_result = set.intersection(first_row, second_row)

    test_case_result = ""
    if len(set_result) == 0:
        test_case_result = NO_SOLUTION
    elif len(set_result) == 1:
        number = set_result.pop()
        test_case_result = number
    else:
        test_case_result = MULTIPLE_SOLUTIONS

    return test_case_result

def solve_problem(input_file, output_file):
    input_file = open(input_file, 'r')
    output_file = open(output_file, 'w+')
    test_cases = int(input_file.readline())
    for i in range(0, test_cases):
        first_row = int(input_file.readline())
        first_arrangement = _read_arrangement(input_file)
        second_row = int(input_file.readline())
        second_arrangement = _read_arrangement(input_file)
        test_case_result = solve_magic_trick(first_row, first_arrangement,
                second_row, second_arrangement)
        test_case = str(i+1)
        output_file.write('Case #' + test_case + ': ' + test_case_result + "\n")
    input_file.close()
    output_file.close()

def _read_arrangement(input_file):
    arrangement = []
    for i in range(0, ARRANGEMENT_SIZE):
        line = input_file.readline()
        numbers = set(line.split())
        arrangement.append(numbers)
    return arrangement

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise Exception('Missing intput/output files')
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    solve_problem(input_file, output_file)
