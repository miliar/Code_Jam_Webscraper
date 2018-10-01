import re
import sys


def read_cases(f):
    f.readline()
    tmp = read_case(f)
    while tmp:
        yield tmp
        tmp = read_case(f)


def read_case(f):
    first = f.readline()
    if not first:
        return None
    second = f.readline()
    third = f.readline()
    fourth = f.readline()
    f.readline()
    return [list(x.strip()) for x in (first, second, third, fourth)]


def x_sqr(sqr):
    return sqr == 'X' or sqr == 'T'


def y_sqr(sqr):
    return sqr == 'O' or sqr == 'T'


def state(board):
    for i in range(4):
        if x_sqr(board[i][0]) and x_sqr(board[i][1]) and x_sqr(board[i][2]) and x_sqr(board[i][3]):
            return "X won"
        if x_sqr(board[0][i]) and x_sqr(board[1][i]) and x_sqr(board[2][i]) and x_sqr(board[3][i]):
            return "X won"
        if y_sqr(board[i][0]) and y_sqr(board[i][1]) and y_sqr(board[i][2]) and y_sqr(board[i][3]):
            return "O won"
        if y_sqr(board[0][i]) and y_sqr(board[1][i]) and y_sqr(board[2][i]) and y_sqr(board[3][i]):
            return "O won"
    if x_sqr(board[0][0]) and x_sqr(board[1][1]) and x_sqr(board[2][2]) and x_sqr(board[3][3]):
        return "X won"
    if x_sqr(board[0][3]) and x_sqr(board[1][2]) and x_sqr(board[2][1]) and x_sqr(board[3][0]):
        return "X won"
    if y_sqr(board[0][0]) and y_sqr(board[1][1]) and y_sqr(board[2][2]) and y_sqr(board[3][3]):
        return "O won"
    if y_sqr(board[0][3]) and y_sqr(board[1][2]) and y_sqr(board[2][1]) and y_sqr(board[3][0]):
        return "O won"
    for i in range(4):
        for j in range(4):
            if board[i][j] == '.':
                return "Game has not completed"
    return "Draw"


def main(argv):
    with open(argv[1]) as f:
        for n, case in enumerate(read_cases(f)):
            print "Case #%d: %s" %(n+1, state(case))


if __name__ == "__main__":
    main(sys.argv)
