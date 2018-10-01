import sys

def is_empty_cells(data):
    for test in data:
        for row in test:
            if '.' in row:
                return True

    return False

def check_winner(s, data):
    # check rows
    for row in data:
        if row.count(s) == 4 or (row.count(s) == 3 and 'T' in row):
            return True

    # check columns
    for i in range(4):
        col = data[0][i] + data[1][i] + data[2][i] + data[3][i]
        if col.count(s) == 4 or (col.count(s) == 3 and 'T' in col):
            return True

    # check diagonals
    diag = data[0][0] + data[1][1] + data[2][2] + data[3][3]
    if diag.count(s) == 4 or (diag.count(s) == 3 and 'T' in diag):
        return True

    diag = data[0][3] + data[1][2] + data[2][1] + data[3][0]
    if diag.count(s) == 4 or (diag.count(s) == 3 and 'T' in diag):
                return True

    return False

def get_status(data):
    if check_winner('O', data):
        return 'O won'
    elif check_winner('X', data):
        return 'X won'
    elif is_empty_cells(data):
        return 'Game has not completed'
    else:
        return 'Draw'

def get_tests(filename):
    f = open(filename, 'r')
    tests = []

    for i in range(int(f.readline())):
        tests.append([])
        for j in range(4):
            tests[-1].append(f.readline()[:-1])

        f.readline()

    return tests

if __name__ == '__main__':
    # read tests from file
    tests = get_tests(sys.argv[1])

    # get state and print it
    for i in range(len(tests)):
        status = get_status(tests[i])
        print('Case #' + str(i + 1) + ': ' + status)
