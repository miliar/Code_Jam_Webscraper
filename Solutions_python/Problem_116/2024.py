T = int(raw_input()) + 1

for i in range (1, T):

    moves = 16
    board = []
    winner = ''
    
    for x in range(0, 4):
        board.append(raw_input())

    X = 0
    O = 0
    T = 0

    for x in range(0, 4):
        X = 0
        O = 0
        T = 0
        for y in range(0, 4):
            if board[x][y] == 'X':
                X = X + 1
            elif board[x][y] == 'O':
                O = O + 1
            elif board[x][y] == 'T':
                T = T + 1
            elif board[x][y] == '.':
                moves = moves - 1
        if X + T == 4:
            winner = 'X'
            break
        elif O + T == 4:
            winner = 'O'
            break

    if winner == '':
        for y in range(0, 4):
            X = 0
            O = 0
            T = 0
            for x in range(0, 4):
                if board[x][y] == 'X':
                    X = X + 1
                elif board[x][y] == 'O':
                    O = O + 1
                elif board[x][y] == 'T':
                    T = T + 1
            if X + T == 4:
                winner = 'X'
                break
            elif O + T == 4:
                winner = 'O'
                break

    if winner == '':
        X = 0
        O = 0
        T = 0
        for x in range(0, 4):
            if board[x][x] == 'X':
                X = X + 1
            elif board[x][x] == 'O':
                O = O + 1
            elif board[x][x] == 'T':
                T = T + 1
        if X + T == 4:
            winner = 'X'
        elif O + T == 4:
            winner = 'O'

    if winner == '':
        X = 0
        O = 0
        T = 0

        y = 3
        for x in range(0, 4):
            if board[x][y] == 'X':
                X = X + 1
            elif board[x][y] == 'O':
                O = O + 1
            elif board[x][y] == 'T':
                T = T + 1
            y = y - 1

        if X + T == 4:
             winner = 'X'
        elif O + T == 4:
            winner = 'O'


    print 'Case #' + str(i) + ': ',
    if winner == '':
        if moves == 16:
            print 'Draw'
        else:
            print 'Game has not completed'
    else:
        print winner + ' won'

    raw_input()
