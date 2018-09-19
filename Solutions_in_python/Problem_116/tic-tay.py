def evalBoard(board):
    x = []
    o = []
    #Horizontal check
    for y in range(4):
        if '.' in board[y]:
            continue
        if 'X' not in board[y]:
            o.append(True)
        elif 'O' not in board[y]:
            x.append(True)
    #Vertical Check
    vert = [False, False, False, False]
    for y in range(4):
        for x1 in range(4):
            if board[x1][y] is '.':
                vert[y] = False
                break
            elif board[x1][y] is 'X':
                if vert[y] is 'O':
                    vert[y] = False
                    break
                vert[y] = 'X'
            elif board[x1][y] is 'O':
                if vert[y] is 'X':
                    vert[y] = False
                    break
                vert[y] = 'O'
    if 'X' in vert:
        x.append(True)
    if 'O' in vert:
        o.append(True)
    #Diagonal Check
    diag = [None, None]
    for y in range(4):
        left = board[left_diagonal[y][1]][left_diagonal[y][0]]
        right = board[right_diagonal[y][1]][right_diagonal[y][0]]
        if left is '.':
                diag[0] = False
        elif left is 'X' and diag[0] is not False:
            if diag[0] is 'O':
                diag[0] = False
            else:
                diag[0] = 'X'
        elif left is 'O' and diag[0] is not False:
            if diag[0] is 'X':
                diag[0] = False
            else:
                diag[0] = 'O'
        if right is '.':
                diag[1] = False
        elif right is 'X' and diag[1] is not False:
            if diag[1] is 'O':
                diag[1] = False
            else:
                diag[1] = 'X'
        elif right is 'O' and diag[1] is not False:
            if diag[1] is 'X':
                diag[1] = False
            else:
                diag[1] = 'O'
    if 'X' in diag:
        x.append(True)
    if 'O' in diag:
        o.append(True)

    return True in x, True in o

cases = int(raw_input())
left_diagonal = [[0, 0], [1,1], [2,2], [3,3]]
right_diagonal = [[0, 3], [1, 2], [2,1], [3, 0]]
for t in range(cases):
    board = []
    x_win = False
    o_win = False
    complete = True
    for row_count in range(4):
        row = raw_input()
        board.append(list(row))
        if '.' in board[row_count]:
            complete = False
    blank = raw_input()
    x_win, o_win = evalBoard(board)
    if x_win is False and o_win is False and complete:
        print "Case #%d: Draw" % (t+1)
    elif o_win:
        print "Case #%d: O won" % (t+1)
    elif x_win:
        print "Case #%d: X won" % (t+1)
    else:
        print "Case #%d: Game has not completed" % (t+1)


