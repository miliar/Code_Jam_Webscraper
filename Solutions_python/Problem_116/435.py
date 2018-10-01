#!/usr/bin/python3

from sys import argv

def print_board(board):
    for i in range(4):
        for j in range(4):
            print(board[4 * i + j], end="")
        print()
    print()

def winner(*line):
    """Return the winner of the game if the line is a win
       for a tic-tac-toe-tomek player. Return None if there
       is no winner for this line.
    >>> winner('X', 'X', 'X', 'X')
    'X'
    >>> winner('T', 'X', 'X', 'X')
    'X'
    >>> winner('X', 'T', 'X', 'X')
    'X'
    >>> winner('X', 'X', 'T', 'X')
    'X'
    >>> winner('X', 'X', 'X', 'T')
    'X'
    >>> winner('.', 'X', 'X', '.')
    >>> winner('X', '.', 'X', 'X')
    >>> winner('X', 'O', '.', 'X')
    >>> winner('T', 'X', 'O', '.')
    >>> winner('O', 'X', 'X', 'X')
    >>> winner('X', 'O', 'X', 'X')
    >>> winner('X', 'X', 'O', 'X')
    >>> winner('X', 'X', 'X', 'O')
    >>> winner('O', 'O', 'O', 'O')
    'O'
    >>> winner('O', 'T', 'O', 'O')
    'O'
    >>> winner('O', 'O', 'X', 'O')
    >>> winner('O', 'O', 'O', '.')
    """
    o, x, t = 0, 0, 0
    for s in line:
        if s == 'O': o += 1
        if s == 'X': x += 1
        if s == 'T': t += 1
    if o + t == 4: return 'O'
    if x + t == 4: return 'X'
    return None

def status(board):
    """Return the status of a Tic-Tac-Toe-Tomek game
     0  1  2  3
     4  5  6  7
     8  9 10 11
    12 13 14 15
    """
    lines = [
        [  0,  1,  2,  3 ],
        [  4,  5,  6,  7 ],
        [  8,  9, 10, 11 ],
        [ 12, 13, 14, 15 ],
        [  0,  4,  8, 12 ],
        [  1,  5,  9, 13 ],
        [  2,  6, 10, 14 ],
        [  3,  7, 11, 15 ],
        [  0,  5, 10, 15 ],
        [  3,  6,  9, 12 ]
    ]
    for l in lines:
        w = winner(board[l[0]], board[l[1]], board[l[2]], board[l[3]])
        if w != None:
            return w + ' won'
    p = 0
    for s in board:
        if s == '.': p += 1
    if p == 0:
        return 'Draw'
    else:
        return 'Game has not completed'

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Google Code Jam I/O
    infile = open(argv[1])
    cases = int(infile.readline())
    for i in range(cases):
        board = []
        for j in range(4):
            board.extend(list(infile.readline().strip()))
        infile.readline()
        print('Case #{}: {}'.format(i+1, status(board)))
