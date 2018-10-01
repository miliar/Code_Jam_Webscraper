#!/usr/bin/env python

import sys

X = "X won"
O = "O won"
D = "Draw"
G = "Game has not completed"

def solve(square):
    seqs = []
    for i in range(4):
        row = [square[i][j] for j in range(4)]
        seqs.append(row)
        col = [square[j][i] for j in range(4)]
        seqs.append(col)
    diag = [square[i][i] for i in range(4)]
    seqs.append(diag)
    diag = [square[i][3-i] for i in range(4)]
    seqs.append(diag)

    has_empty = False
    for seq in seqs:
        which = {'.':False, 'X':False, 'O':False, 'T':False}
        for c in seq:
            which[c] = True
        if which['.']:
            has_empty = True
        else:
            if which['X'] is not which['O']:
                return which['X'] and X or O
    return has_empty and G or D

def gen_square():
    square = []
    for j in range(4):
        square.append(str(sys.stdin.readline()).rstrip())
    sys.stdin.readline()
    return square

def main():
    tests = int(str(sys.stdin.readline()).rstrip())
    i = 1
    while i <= tests:
        square = gen_square()
        result = solve(square)
        print 'Case #{0}: {1}'.format(i, result)
        i += 1

if __name__ == "__main__":
    main()
