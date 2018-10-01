FILE_NAME_PREFIX = 'A-small-attempt0'
RESULT_STRING_AMBIGUOUS = "Bad magician!"
RESULT_STRING_CHEATED = "Volunteer cheated!"


def find_common_number(first_row, second_row):
    common = -1
    for first_col in range(4):
        first_val = first_row[first_col]
        for second_col in range(4):
            second_val = second_row[second_col]
            if first_val == second_val:
                if common != -1:
                    return RESULT_STRING_AMBIGUOUS
                common = first_val
                break

    if common == -1:
        return RESULT_STRING_CHEATED

    return common


if __name__ == '__main__':
    input_file = open('in/' + FILE_NAME_PREFIX + '.in', 'r')
    output_file = open('out/' + FILE_NAME_PREFIX + '.out', 'w')
    test_case_nb = int(input_file.readline())

    for case in range(test_case_nb):
        first_grid_row = int(input_file.readline())
        first_grid = [[int(x) for x in input_file.readline().split()] for _ in range(4)]
        second_grid_row = int(input_file.readline())
        second_grid = [[int(x) for x in input_file.readline().split()] for _ in range(4)]
        res = find_common_number(first_grid[first_grid_row - 1], second_grid[second_grid_row - 1])

        output_file.write("Case #" + str(case + 1) + ": " + str(res) + '\n')

    input_file.close()
    output_file.close()

