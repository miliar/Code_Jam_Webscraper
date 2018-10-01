import numpy as np

def set_or(possible, number_set):
    possible |= number_set

def set_and(possible, number_set):
    possible &= number_set

def solve(i, lines, output_file):
    possible = set()
    answer = int(lines.pop(0))
    parse_array(lines, answer, set_or, possible)
    answer = int(lines.pop(0))
    parse_array(lines, answer, set_and, possible)

    row = "Case #%i: " % i

    if not possible:
        output_file.write(row + "Volunteer cheated!\n")
    elif len(possible) == 1:
        output_file.write(row + str(possible.pop()) + "\n")
    else:
        output_file.write(row + "Bad magician!\n")

def parse_array(lines, row, fn, possible):
    for i in range(4):
        line = lines.pop(0)
        if (i + 1 == row):
            number_set = set([int(n) for n in line.split()])
            fn(possible, number_set)

if __name__ == "__main__":
    filename = 'magic_trick.txt'
    output_filename = 'magic_trick_output.txt'

    lines = open(filename, 'r').readlines()
    test_cases = int(lines.pop(0))
    output_file = open(output_filename, 'w')

    for i in range(test_cases):
        solve(i+1, lines, output_file)

    output_file.close()
