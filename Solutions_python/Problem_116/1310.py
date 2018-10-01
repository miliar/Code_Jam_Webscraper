#!/usr/bin/python


def Win(board):
    for i in xrange(4):
        if board[i][0] == board[i][1] == board[i][2] == board[i][3] != "." or board[0][i] == board[1][i] == board[2][i] == board[3][i] != "." \
           or board[i][0] == 'T' and board[i][1] == board[i][2] == board[i][3] != "." or board[0][i] == 'T' and board[1][i] == board[2][i] == board[3][i] != "." \
           or board[i][1] == 'T' and board[i][0] == board[i][2] == board[i][3] != "." or board[1][i] == 'T' and board[0][i] == board[2][i] == board[3][i] != "." \
           or board[i][2] == 'T' and board[i][1] == board[i][0] == board[i][3] != "." or board[2][i] == 'T' and board[1][i] == board[0][i] == board[3][i] != "." \
           or board[i][3] == 'T' and board[i][1] == board[i][2] == board[i][0] != "." or board[3][i] == 'T' and board[1][i] == board[2][i] == board[0][i] != ".":
            winner1 = [board[i][0], board[i][1], board[i][2], board[i][3]]
            winner2 = [board[0][i], board[1][i], board[2][i], board[3][i]]
            if 'T' in winner1:
                winner1.remove('T')
            if 'T' in winner2:
                winner2.remove('T')
            winner1 = list(set(winner1))
            winner2 = list(set(winner2))
            if len(winner1) == 1 and winner1[0] != '.':
                winner = winner1[0]
            elif len(winner2) == 1 and winner2[0] != '.':
                winner = winner2[0]
            print winner, "won"
            return True

    if board[0][0] == board[1][1] == board[2][2] == board[3][3] != "." \
       or board[0][0] == 'T' and board[1][1] == board[2][2] == board[3][3] != "." \
       or board[1][1] == 'T' and board[0][0] == board[2][2] == board[3][3] != "." \
       or board[2][2] == 'T' and board[1][1] == board[0][0] == board[3][3] != "." \
       or board[3][3] == 'T' and board[1][1] == board[2][2] == board[0][0] != ".":
        winner = [board[0][0], board[1][1], board[2][2], board[3][3]]
        if 'T' in winner:
            winner.remove('T')
        winner = list(set(winner))
        print winner[0], "won"
        return True

    if board[0][3] == board[1][2] == board[2][1] == board[3][0] != "." \
       or board[0][3] == 'T' and board[1][2] == board[2][1] == board[3][0] != "." \
       or board[1][2] == 'T' and board[0][3] == board[2][1] == board[3][0] != "." \
       or board[2][1] == 'T' and board[1][2] == board[0][3] == board[3][0] != "." \
       or board[3][0] == 'T' and board[1][2] == board[2][1] == board[0][3] != ".":
        winner = [board[0][3], board[1][2], board[2][1], board[3][0]]
        if 'T' in winner:
            winner.remove('T')
        winner = list(set(winner))
        print winner[0], "won"
        return True
    return False


def Draw(board):
    for row in board:
        if '.' in row:
            return False
    print "Draw"
    return True


T = input()
for i in xrange(T):
    board = [['.'] * 4] * 4
    for j in xrange(4):
        board[j] = list(raw_input())
    if i < T-1:
        raw_input()
    print "Case #" + str(i + 1) + ":",
    if not Win(board):
        if not Draw(board):
            print "Game has not completed"
