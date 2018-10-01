__author__ = 'sean223'


# IN_FILE = 'test_input.txt'
# OUT_FILE = 'test_output.txt'

# IN_FILE = 'A-small.in'
# OUT_FILE = 'small_out.txt'

IN_FILE = 'A-large.in'
OUT_FILE = 'large_out.txt'


with open(IN_FILE, 'r') as fileIn:
    fileLines = fileIn.readlines()

it = iter(fileLines)
numbCases = int(next(it))
output = ""


for case in range(1, numbCases+1):
    r, c = [int(x) for x in next(it).strip().split()]

    grid = []

    for _i in range(r):
        grid.append(list(next(it).strip()))

    for j, row in enumerate(grid):
        if row.count('?') < c:
            first_letter = ''
            for letter in row:
                if letter is not '?':
                    first_letter = letter
                    break
            for i, letter in enumerate(row):
                if letter == '?':
                    if i == 0:
                        row[i] = first_letter
                    else:
                        row[i] = row[i-1]

    first_non_empty_row = []
    for row in grid:
        if '?' not in row:
            first_non_empty_row = row
            break

    for j, row in enumerate(grid):
        if '?' in row:
            if j == 0:
                grid[j] = first_non_empty_row
            else:
                grid[j] = grid[j-1]

    answer = ''

    line = "Case #{0}: \n".format(str(case))
    for row in grid:
        line += ''.join(row) + '\n'
    output += line


with open(OUT_FILE, 'w') as fileOut:
    fileOut.write(output)
