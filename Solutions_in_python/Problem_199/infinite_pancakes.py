import fileinput

no_of_tests = None

case_number = 1
happy_face = '+'
blank_face = '-'


def flip_pancakes(index, test_line, flipper_size):
    for i in range(index, index + flipper_size):
        if test_line[i] is happy_face:
            test_line[i] = '-'
        elif test_line[i] is blank_face:
            test_line[i] = '+'

    return test_line

for line in fileinput.input():

    if len(line) < 1:
        continue

    if no_of_tests is None:
        no_of_tests = int(line)
        continue

    test_line = list(line.split()[0])
    flipper_size = int(line.split()[1])
    number_of_flips = 0

    line_size = len(test_line)

    if flipper_size > line_size:
        print('Case #' + str(case_number) + ': IMPOSSIBLE')
        case_number += 1
        continue

    for i in range(0, line_size - (flipper_size - 1)):
        if test_line[i] is blank_face:
            test_line = flip_pancakes(i, test_line, flipper_size)
            number_of_flips += 1

    if blank_face in test_line:
        print('Case #' + str(case_number) + ': IMPOSSIBLE')
        case_number += 1
        continue

    else:
        print('Case #' + str(case_number) + ': ' + str(number_of_flips))
        case_number += 1
        continue