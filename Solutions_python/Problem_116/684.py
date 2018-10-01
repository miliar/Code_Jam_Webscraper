#!/usr/bin/python

import sys

def winner(player, board):
    target_row = player * 4
    for row in board:
        if row.replace("T", player) == target_row:
            return True
    return False

def full(board):
    for row in board[:4]:
        if "." in row:
            return False
    return True

def main():
    for tc_num in xrange(int(sys.stdin.readline())):
        board = [sys.stdin.readline().strip() for _ in xrange(4)]
        board.extend(board[0][i] + board[1][i] + board[2][i] + board[3][i] for i in xrange(4))
        board.append(board[0][0] + board[1][1] + board[2][2] + board[3][3])
        board.append(board[0][3] + board[1][2] + board[2][1] + board[3][0])
        sys.stdin.readline()
        print "Case #%d:" % (tc_num + 1),
        if winner("X", board):
            print "X won"
        elif winner("O", board):
            print "O won"
        elif full(board):
            print "Draw"
        else:
            print "Game has not completed"

if __name__ == "__main__":
    main()
