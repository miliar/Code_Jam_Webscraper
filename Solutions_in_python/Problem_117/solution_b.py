#!/usr/bin/python

import sys
import copy

class Board(object):
    def __init__(self, dimension_list, board_string):
        self.dimension_list = dimension_list
        self.board_string = board_string
        self.board = self._convert_board_to_list()
        self.m = self._reverse_populate_m()
        self.n = self._reverse_populate_n()
        self.rebuilt_board = self._rebuild()
        self.valid = self._set_valid()

    def is_valid(self):
        if self.valid:
            return "YES"
        return "NO"

    def _set_valid(self):
        if self.board_string == self.rebuilt_board:
            return True
        return False

    def _rebuild(self):
        # init the board
        new_board = []
        for i in range(int(self.dimension_list[0])):
            new_board.append([])
            for j in range(int(self.dimension_list[1])):
                new_board[i].append(100)
                new_board[i][j] = min(self.m[j], self.n[i])

        board_string = ''
        for i in new_board:
            board_string += ' '.join(i) + "\n"

        return board_string



    def _reverse_populate_n(self):
        new_indecies = []
        for column in self.board:
            new_indecies.append(self._max_in_list(column))

        return new_indecies

    def _reverse_populate_m(self):
        new_indecies = []
        for i in range(int(self.dimension_list[1])):
            row_list = []
            for j in range(int(self.dimension_list[0])):
                row_list.append(self.board[j][i])

            new_indecies.append(self._max_in_list(row_list))

        return new_indecies

    def _convert_board_to_list(self):
        rows = self.board_string.splitlines()
        new_board = []
        for row in rows:
            new_board.append(row.split())

        return new_board

    def _max_in_list(self, search_list):
        list = search_list[:]
        try:
            list.sort()
        except:
            pass
        return list[-1]

    def __str__(self):
        string = "M: " + repr(self.m) + "\nN: " + repr(self.n) + "\n" + self.board_string + "\n" + self.rebuilt_board
        return string
try:
    source_file = open(sys.argv[1], 'r')
except:
    print 'Error opening file'
    sys.exit(0)

line = source_file.readline()
total_cases = int(line)

# read file
cases = []
board_string = ''

while 1:
    line = source_file.readline()
    if not line:
        break

    dimensions_string = line
    dimensions_list = line.split()
    for i in range(int(dimensions_list[0])):
        board_string += source_file.readline()
    cases.append(Board(dimensions_list, board_string))
    board_string = ''


#print "total cases: %s" % total_cases
#print "number found: %s" % len(cases)

i = 1;
for case in cases:
    print "Case #%s: %s" % (i, case.is_valid())
    i += 1
