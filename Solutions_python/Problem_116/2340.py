def read(filename):
    input = open(filename, 'r')
    lines = []
    for line in input:
        lines.append(line.rstrip('\n')) # strip out the newline characters
    return lines

def check_board(board):
    for i in range(4):  # check rows
        row = board[i]
        if check(row, 'X'):
            return 'X won'
        if check(row, 'O'):
            return 'O won'
    for j in range(4):  # check columns
        col = []
        for k in range(4):
            col.append(board[k][j])
        if check(col, 'X'):
            return 'X won'
        if check(col, 'O'):
            return 'O won'
    if check_diag(1, board, 'X'):  # check diagonal 1
        return 'X won'
    if check_diag(1, board, 'O'):
        return 'O won'
    if check_diag(2, board, 'X'):  # check diagonal 2
        return 'X won'
    if check_diag(2, board, 'O'):
        return 'O won'
    dots = ''.join(board).count('.')
    if dots == 0:   # no dots left = Draw
        return 'Draw'
    return 'Game has not completed'

def check(input, value):
    num = input.count(value)
    t = input.count('T')
    return num + t == 4

def check_diag(index, board, value):
    diag = []
    for i in range(4):
        if index == 1:
            diag.append(board[i][i])
        else:
            diag.append(board[i][3 - i])
    return check(diag, value)

def main():
    lines = read('A-large.in')
    num = int(lines.pop(0))
    line_num = 0
    for i in range(num):
        board = lines[line_num:line_num + 4]
        print("Case #" + str(i + 1) + ": " + str(check_board(board)))
        line_num += 5

if __name__ == '__main__':
    main()
