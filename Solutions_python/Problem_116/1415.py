__author__ = 'joranvar'
__problem__ = 'A'

import sys


class Board(object):
    def __init__(self, data):
        self.data = data
        self.size = len(data)

    def won(self, marks):
        hits = [[square in marks for square in line] for line in self.data]
        over_x = any([all([hits[x][y] for x in range(self.size)]) for y in range(self.size)])
        if over_x: return True
        over_y = any([all([hits[x][y] for y in range(self.size)]) for x in range(self.size)])
        if over_y: return True
        over_xy = all([hits[x][x] for x in range(self.size)])
        if over_xy: return True
        over_yx = all([hits[x][self.size - 1 - x] for x in range(self.size)])
        return over_yx

    def contains(self, square):
        return square in ''.join(''.join(x) for x in self.data)


def read_board(f_in, size):
    board_data = [[square for square in f_in.readline()[:-1]] for line in range(size)]
    empty_line = f_in.readline()
    board = Board(board_data)
    return board

def solve(case, f_in):
    board = read_board(f_in, 4)
    if board.won('XT'): return ['Case #{}: X won\n'.format(case + 1)]
    if board.won('OT'): return ['Case #{}: O won\n'.format(case + 1)]
    if board.contains('.'): return ['Case #{}: Game has not completed\n'.format(case + 1)]
    return ['Case #{}: Draw\n'.format(case + 1)]

if __name__ == '__main__':
    f_in = open(sys.argv[1], 'r')
    f_out = open(__problem__ + '.out', 'w')
    T = int(f_in.readline())
    for case in range(T):
        f_out.writelines(solve(case, f_in))