#! /usr/bin/env python
import sys
from collections import Counter

class Board(object):
    def __init__(self, board_string):
        self.state = [board_string[4*i:4*i+4] for i in xrange(4)]
    
    def get_col(self, i):
        return [self.state[j][i] for j in xrange(4)]
    
    def get_row(self, i):
        return list(self.state[i])
        
    def get_uldr(self):
        return [self.state[i][i] for i in xrange(4)]
    
    def get_urdl(self):
        return [self.state[i][3-i] for i in xrange(4)]
    
    def get_whole(self):
        return ''.join(self.state)

def read_file():
    # return a list of boards
    with open(sys.argv[1]) as data_file:
        boards = [[] for _ in xrange(int(data_file.readline()))]
        for i in xrange(len(boards)):
            board_string = ''
            for _ in xrange(4):
                board_string = ''.join([board_string, data_file.readline().strip()])
            data_file.readline()
            boards[i] = Board(board_string)
    return boards

def determine_board_state(current_board):
    # Return (completed, winner) : boolean, string
    for i in xrange(4):
        col = Counter(current_board.get_col(i))
        row = Counter(current_board.get_row(i))
        if col['X'] == 4 or col['X'] == 3 and col['T'] == 1:
            return True, 'X'
        elif row['X'] == 4 or row['X'] == 3 and row['T'] == 1:
            return True, 'X'
        elif col['O'] == 4 or col['O'] == 3 and col['T'] == 1:
            return True, 'O'
        elif row['O'] == 4 or row['O'] == 3 and row['T'] == 1:
            return True, 'O'
    diag = Counter(current_board.get_uldr())
    if diag['X'] == 4 or diag['X'] == 3 and diag['T'] == 1:
        return True, 'X'
    if diag['O'] == 4 or diag['O'] == 3 and diag['T'] == 1:
        return True, 'O'
    diag = Counter(current_board.get_urdl())
    if diag['X'] == 4 or diag['X'] == 3 and diag['T'] == 1:
        return True, 'X'
    if diag['O'] == 4 or diag['O'] == 3 and diag['T'] == 1:
        return True, 'O'

    if Counter(current_board.get_whole())['.']:
        return False, None
    else:
        return True, None

def main():
    boards = read_file()
    results = [[] for _ in xrange(len(boards))]
    for i, board in enumerate(boards):
        results[i] = determine_board_state(board)

    with open(sys.argv[2], 'w') as out_file:
        for i, result in enumerate(results, start=1):
            out_string = 'Case #{}: '.format(i)
            if result[0]: # Game completed
                winner = result[1]
                if winner: # Game is not a draw
                    out_string += winner + ' won'
                else:
                    out_string += 'Draw'
            else:
                out_string += 'Game has not completed'
            out_file.write(out_string + '\n')

if __name__ == '__main__':
    # run as $ python tttt.py input.txt output.txt
    main()
