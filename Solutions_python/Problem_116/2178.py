__author__ = 'wonglik'




cases = 0
in_progress = False
win = ''

board =  [['' for x in xrange(4)] for x in xrange(4)]

def column(matrix, i):
    return [row[i] for row in matrix]

def diagonal_left(matrix):

    return [row[i] for i , row in enumerate(matrix)]

def diagonal_right(matrix):
    return [row[3-i] for i , row in enumerate(matrix)]

def find_winer_in_row(row):

    if '.' in row:
        return '.'
    count_t = row.count('T')
    count_o = row.count('O')

    if (count_o+count_t) == 4:
        return 'O'

    count_x = row.count('X')

    if (count_x+count_t) == 4:
        return 'X'

    return None

def find_winer_in_column(c):

    row = column(board,c)
    return find_winer_in_row(row)

def find_winer_in_left_diagonal(board):
    row = diagonal_left(board)
    return find_winer_in_row(row)

def find_winer_in_right_diagonal(board):
    row = diagonal_right(board)
    return find_winer_in_row(row)

def find_winner(board):
    winer = None
    in_progress = None
    for i in xrange(4):
        w = find_winer_in_row(board[i])
        if w == '.':
            in_progress = '.'
        else:
            if w is not None:
                return w
    for j in xrange(4):
        w = find_winer_in_column(j)
        if w == '.':
            in_progress = '.'
        else:
            if w is not None:
                return w

    w = find_winer_in_left_diagonal(board)
    if w == '.':
        in_progress = '.'
    else:
        if w is not None:
            return w

    w = find_winer_in_right_diagonal(board)
    if w == '.':
        in_progress = '.'
    else:
        if w is not None:
            return w


    if in_progress is not None:
        return '.'

    return None



f = open('A-large.in', 'r')
fw = open('output', 'w')
lines = f.readlines()
cases = int(lines[0].strip())

for idx , line in enumerate(lines[1:]):
    # print idx % 5 , line.strip()
    if line != '\n':

        for i,c in enumerate(line.strip()):
            board[(idx % 5)][i] = c
    else:
        w= find_winner(board)
        case = idx // 5 +1
        if w is None:
            fw.write('Case #'+str(case)+': Draw')
            fw.write('\n')
            continue
        if w is '.':
            fw.write('Case #'+str(case)+': Game has not completed')
            fw.write('\n')
            continue
        fw.write('Case #'+str(case)+': '+w+' won')
        fw.write('\n')

f.close()
fw.close()



