import sys


def solve_test(answer1, arrangement1, answer2, arrangement2):
    row1 = arrangement1[answer1 - 1]
    row2 = arrangement2[answer2 - 1]
    # check if a number is in both
    matches = 0
    for card in row1:
        if card in row2:
            matches += 1
            match = card
    if matches == 0:
        return "Volunteer cheated!"
    if matches > 1:
        return "Bad magician!"
    return match

if __name__ == "__main__":
    lines = [line.rstrip('\n') for line in open(sys.argv[1])]
    f = open('out.txt', 'w')
    number_of_tests = int(lines[0])
    line_count = 1
    # for each test
    for test_number in range(1, number_of_tests + 1):
        first_answer = int(lines[line_count])
        line_count += 1
        first_row = [int(i) for i in lines[line_count].split(' ')]
        line_count += 1
        second_row = [int(i) for i in lines[line_count].split(' ')]
        line_count += 1
        third_row = [int(i) for i in lines[line_count].split(' ')]
        line_count += 1
        fourth_row = [int(i) for i in lines[line_count].split(' ')]
        line_count += 1
        first_arrangement = [first_row, second_row, third_row, fourth_row]

        second_answer = int(lines[line_count])
        line_count += 1
        first_row = [int(i) for i in lines[line_count].split(' ')]
        line_count += 1
        second_row = [int(i) for i in lines[line_count].split(' ')]
        line_count += 1
        third_row = [int(i) for i in lines[line_count].split(' ')]
        line_count += 1
        fourth_row = [int(i) for i in lines[line_count].split(' ')]
        line_count += 1
        second_arrangement = [first_row, second_row, third_row, fourth_row]

        f.write('Case #%s: %s\n' % (test_number, solve_test(first_answer, first_arrangement, second_answer, second_arrangement)))
        test_number += 1
    f.close()
