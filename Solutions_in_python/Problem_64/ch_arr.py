#!/usr/bin/env python

from functools import wraps
import numpy as np

CUT = 2
range = xrange

def memoized(f):
    f.cache = {}
    @wraps(f)
    def g(*args):
      if args not in f.cache:
          f.cache[args] = f(*args)
      return f.cache[args]
    return g

# Big arrays of chessboard patterns.
# Smaller masks are views into these arrays
even_array = np.fromfunction((lambda i, j: (i + j + 0) % 2), shape=(512, 512), dtype='int32')
odd_array  = np.fromfunction((lambda i, j: (i + j + 1) % 2), shape=(512, 512), dtype='int32')

@memoized
def patterns(n):
    return even_array[:n, :n], odd_array[:n, :n]


def find_board(size, i, j, board):
    "Is there a board of the given size at (i, j)?"
    m, n = board.shape
    even, odd = patterns(size)
    view = board[i:i+size, j:j+size]
    return (view == even).all() or (view == odd).all()

def cut_out_board(size, i, j, board):
    board[i:i+size, j:j+size] = CUT


def cutouts(board):
    m, n = board.shape
    cuts = []
    for size in range(min(m, n), 1, -1):
        nr_cuts = 0

        for i in range(m - size + 1):
            for j in range(n - size + 1):
                if find_board(size, i, j, board):
                    #print "Found at {0}, {1} of size {2}".format(i, j, size)
                    cut_out_board(size, i, j, board)
                    nr_cuts += 1
                    #print board

        if nr_cuts:
            cuts.append((size, nr_cuts))


    o = (board == 1).sum() + (board == 0).sum()
    if o:
        cuts.append((1, o))

    return cuts

def hex_to_row(row, N):
    n = int(row, 16)
    b = bin(n)[2:]
    return (N - len(b)) * [0] + map(int, b)


try: raw_input
except NameError: pass
else: input = raw_input

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        M, N = map(int, input().split())
        grid = [hex_to_row(input(), N) for _ in range(M)]

        boards = cutouts(np.array(grid, dtype='int32'))
        K = len(boards)
        print('Case #{0}: {1}'.format(t, K))
        for size, nr_boards in boards:
            print('{0} {1}'.format(size, nr_boards))

