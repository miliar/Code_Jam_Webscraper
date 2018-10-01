#!/usr/bin/env python
"""Solve problem A"""
from itertools import count

def identity(x):
    """The identity function"""
    return x

def transpose(x):
    """Calculate the transpose of x
    >>> transpose([[1,2,3],[3,4,5],[5,6,7]])
    [(1, 3, 5), (2, 4, 6), (3, 5, 7)]
    """
    return zip(*x)

def diagonals(table):
    """Return the diagonals from the table
    >>> diagonals([[1,2,3],[3,4,5],[5,6,7]])
    [[1, 4, 7], [3, 4, 5]]
    """
    result = [[], []]
    i = 0
    for i in count():
        x = i
        y = i
        try:
            point = table[x][y]
        except LookupError:
            break
        result[0].append(point)

    max_i = i - 1
    for j in count():
        x = j
        y = max_i - j
        try:
            point = table[x][y]
        except LookupError:
            break
        result[1].append(point)
    return result


def check_row(row):
    """Check a singular row for a tic-tac-toe-tomek win
    >>> print check_row('.XOT')
    Game has not completed
    >>> print check_row('XXXT')
    X won
    >>> print check_row('OTOO')
    O won
    >>> print check_row('XTOX')
    None
    """
    row = ''.join(row)
    if '.' in row:
        return Board.STATES.IN_PROGRESS
    row = row.replace('T', '')

    if not row.strip('X'):
        return Board.STATES.X_WINS
    if not row.strip('O'):
        return Board.STATES.O_WINS

    return None


class Board(object):
    """Represent a tic-tac-toe-tomek board"""
    class STATES: # missing __init__:pylint: disable=W0232
        """An enumeration of possible states"""
        IN_PROGRESS = 'Game has not completed'
        X_WINS = 'X won'
        O_WINS = 'O won'
        DRAW = 'Draw'
    WIN_STATES = (STATES.X_WINS, STATES.O_WINS)

    def __init__(self, boardlines):
        self.boardlines = boardlines

    @property
    def state(self):
        """The current state of the board"""
        final_state = Board.STATES.DRAW
        for transform in (
                identity,
                transpose,
                diagonals,
        ):
            rows = transform(self.boardlines)
            for row in rows:
                rowstate = check_row(row)
                if rowstate in Board.WIN_STATES:
                    return rowstate
                elif rowstate:
                    final_state = rowstate
        else:
            return final_state

    def __str__(self):
        return '\n'.join(self.boardlines)


def solve(infile):
    """Perform the solution"""
    infile = iter(infile)
    case_number = 1

    next(infile) # Skip the first line

    while True:
        board = []
        for _ in range(4):
            try:
                board.append(next(infile).strip())
            except StopIteration:
                return
        board = Board(board)
        print 'Case #%i:' % case_number, board.state
        case_number += 1

        try:
            next(infile) # Skip the blank line.
        except StopIteration:
            return


def main():
    """our entry point"""
    from sys import argv
    fname = argv[1]
    fd = open(fname)
    solve(fd)


if __name__ == '__main__':
    main()
