#!/usr/bin/env python
# -*- coding: utf-8 -*


def winner(part):
    out = ""

    if "." not in part:
        if "T" in part:
            ti =  part.index("T")
            if part[:ti] + part[ti+1:] in ["X"*3, "O"*3]:
                out = part[ti-1] + " won"
        elif part in ["X"*4, "O"*4]:
            out = part[0] + " won"

    return out, out != ""


def solve(board):
    draw = False

    for i in range(4):
        line = board[i]
        draw += "." in line
        out, solved = winner(line)
        if solved:
            break

        col = "".join(board[j][i] for j in range(4))
        out, solved = winner(col)
        if solved:
            break

    if not solved:
        diag = "".join(board[i][i] for i in range(4))
        out, solved = winner(diag)
    if not solved:
        antidiag = "".join(board[i][3-i] for i in range(4))
        out, solved = winner(antidiag)

    if not solved:
        if draw:
            out = "Game has not completed"
        else:
            out = "Draw"

    return out


if __name__ == "__main__":
    T = int(input())  # nb of test cases

    for x in range(T):
        board = [input() for i in range(4)]  # 4x4 board

        y = solve(board)
        print("Case #%d: %s" % (x+1, y))
        input()  # empty line
