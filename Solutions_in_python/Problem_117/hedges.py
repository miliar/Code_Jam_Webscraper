import numpy
import itertools

__author__ = 'tmehta'

file = open('B-large.in', 'r')
out = open('output_hedges.txt', 'w')
number_of_cases = file.readline()
lines = file.readlines()
output = ""


def check_hedges(yard):
    n = len(yard)
    if n == 1:
        return "YES"
    if yard[0][-1] == "\n":
        first_row = yard[0][:-1].split(" ")
    else:
        first_row = yard[0][:].split(" ")
    m = len(first_row)
    if m == 1:
        return "YES"
    row = map(lambda x: int(x), first_row)
    array = numpy.array(row)
    for i in range(1, n):
        row = map(lambda x: int(x), yard[i][:-1].split(" "))
        array = numpy.vstack((array, numpy.array(row)))

    for i, j in itertools.product(range(n), range(m)):
        element = array[i, j]
        row_elements = array[i, :]
        something_same = False
        if array[i, 0] <= element and j != 0:
            something_same = True
        if array[i, m - 1] <= element and j != m - 1:
            something_same = True
        if array[0, j] <= element and i != 0:
            something_same = True
        if array[n - 1, j] <= element and i != n - 1:
            something_same = True
        for k, row_element in enumerate(row_elements):
            if row_element > element:
                column_elements = array[:, j]
                for k, col_element in enumerate(column_elements):
                    if col_element > element:
                        something_same = False
                break
        if not something_same:
            return "NO"
    return "YES"


line_at = 0
for i in range(int(number_of_cases)):
    num_lines = int(lines[line_at].split(" ")[0])
    yard = lines[line_at + 1:line_at + 1 + num_lines]
    game_status = check_hedges(yard)
    line_at = line_at + 1 + num_lines
    output += "Case #" + str(i + 1) + ": " + game_status + "\n"

out.write(output)
