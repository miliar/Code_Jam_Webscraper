#!/usr/bin/env python
import sys
import numpy

case = 1

def check_for_win(row):
    last_xo = None
#    print row
    for c in row:
        if c == '.':
            return None
        if c != 'T':
            if last_xo == None:
                last_xo = c
            elif c != last_xo:
                return None
    return last_xo

def check_for_wins(board):
    for row in board:
        winner = check_for_win(row)
        if winner:
            print 'Case #' + str(case) + ': ' + winner + ' won'
            return True
    return False

def process_board(b):
    if check_for_wins(b) \
            or check_for_wins(numpy.transpose(b)) \
            or check_for_wins([[b[0][0], b[1][1], b[2][2], b[3][3]]]) \
            or check_for_wins([[b[0][3], b[1][2], b[2][1], b[3][0]]]):
        return
    incomplete_board = len([row for row in b if '.' in row]) > 0
    if incomplete_board:
        print 'Case #' + str(case) + ': Game has not completed'
    else:
        print 'Case #' + str(case) + ': Draw'

def chunks(l):
    for i in xrange(0, len(l), 5):
        yield l[i:i+4]

lines = sys.stdin.readlines()

boards = list(chunks([[c for c in line.strip()] for line in lines[1:]]))

for board in boards:
    process_board(board)
    case += 1
