import sys

STR_X_WON = "X won"
STR_DRAW = "Draw"
STR_NOT_COMPLETED = "Game has not completed"
STR_O_WON = "O won"


def answer(case, board):
    dot_found = False
    dp = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == ".":
                dot_found = True
                dp.append([False, False])
            elif board[i][j] == "T":
                up = True
                if i - 1 >= 0:
                    up = dp[(i-1)*4+j][0]
                left = True
                if j - 1 >= 0:
                    left = dp[i*4+(j-1)][1]
                dp.append([up, left])
            else:
                up = True
                if i - 1 >= 0:
                    up = (dp[(i-1)*4+j][0] and (board[i][j] == board[i-1][j] or board[i-1][j] == "T"))
                left = True
                if j - 1 >= 0:
                    left = (dp[i*4+(j-1)][1] and (board[i][j] == board[i][j-1] or board[i][j-1] == "T"))
                dp.append([up, left])
            if j == 3 and dp[-1][1]:
                if board[i][j] == "X" or board[i][j-1] == "X":
                    return "Case #{0}: {1}".format(case, STR_X_WON)
                elif board[i][j] == "O" or board[i][j-1] == "O":
                    return "Case #{0}: {1}".format(case, STR_O_WON)
            if i == 3 and dp[-1][0]:
                if board[i][j] == "X" or board[i-1][j] == "X":
                    return "Case #{0}: {1}".format(case, STR_X_WON)
                elif board[i][j] == "O" or board[i-1][j] == "O":
                    return "Case #{0}: {1}".format(case, STR_O_WON)

    up_left = True
    for i in range(4):
        if board[i][i] == ".":
            up_left = False
            break
        elif board[i][i] == "T":
            continue
        else:
            if i - 1 >= 0:
                if board[i][i] == board[i-1][i-1] or board[i-1][i-1] == "T":
                    continue
                else:
                    up_left = False
                    break
    if up_left:
        if board[0][0] == "X" or board[1][1] == "X":
            return "Case #{0}: {1}".format(case, STR_X_WON)
        elif board[0][0] == "O" or board[1][1] == "O":
            return "Case #{0}: {1}".format(case, STR_O_WON)

    up_right = True
    for i in range(4):
        if board[i][3-i] == ".":
            up_right = False
            break
        elif board[i][3-i] == "T":
            continue
        else:
            if i - 1 >= 0:
                if board[i][3-i] == board[i-1][3-(i-1)] or board[i-1][3-(i-1)] == "T":
                    continue
                else:
                    up_right = False
                    break
    if up_right:
        if board[0][3] == "X" or board[1][2] == "X":
            return "Case #{0}: {1}".format(case, STR_X_WON)
        elif board[0][3] == "O" or board[1][2] == "O":
            return "Case #{0}: {1}".format(case, STR_O_WON)

    if dot_found:
        return "Case #{0}: {1}".format(case, STR_NOT_COMPLETED)
    else:
        return "Case #{0}: {1}".format(case, STR_DRAW)


def main():
    casenum = int(sys.stdin.readline())
    for case in range(casenum):
        board = []
        for i in range(4):
            board.append(list(sys.stdin.readline()))
        print answer(case+1, board)
        sys.stdin.readline()


if __name__ == "__main__":
    main()
