#!/usr/bin/python2
# -*- coding: utf8 -*-
# Google Code Jam 2013 - Qualification Round - Problem A - Mateusz Kurek
# import io
# import numpy as np
from collections import defaultdict, deque

# raw_input = input
# xrange = range


def read_ints():
    return map(int, raw_input().strip().split())


class Solver(object):
    def solve_case(self):
        self.lawn = []
        self.heights = defaultdict(int)
        self.available_heights = set()
        self.lowest_h = 100

        rows, cols = self.current_size = read_ints()

        for r in range(rows):
            row = read_ints()
            for col, h in enumerate(row):
                self.heights[h] += 1
                self.lowest_h = min(h, self.lowest_h)
                self.available_heights.add(h)
            self.lawn.append(row)

        self.available_heights = deque(sorted(list(self.available_heights)))

        # try to remove rows and cols with lowest height
        while(self.lawn and self.try_to_remove()):
            pass

        return not self.lawn

    def get_row(self, row):
        col_size, row_size = self.current_size
        return self.lawn[row]

    def get_col(self, col):
        col_size, row_size = self.current_size
        return [row[col] for row in self.lawn]

    def get_lowest_place(self, h):
        for row_nr, row in enumerate(self.lawn):
            for col, pl_h in enumerate(row):
                if pl_h == h:
                    yield (row_nr, col)

    def del_row(self, row):
        row_h = self.lawn[row][0]
        self.lawn.pop(row)
        self.heights[row_h] -= self.current_size[1]
        self.current_size = (self.current_size[0]-1, self.current_size[1])
        if not self.heights[row_h]:
            self.available_heights.popleft()
            self.lowest_h = self.available_heights[0] if self.available_heights else -1

    def del_col(self, col):
        col_h = self.lawn[0][col]
        for row in self.lawn:
            row.pop(col)
        self.heights[col_h] -= self.current_size[0]
        self.current_size = (self.current_size[0], self.current_size[1]-1)
        if not self.heights[col_h]:
            self.available_heights.popleft()
            self.lowest_h = self.available_heights[0] if self.available_heights else -1

    def try_to_remove(self):
        """
        Tries to remove row/column with the lowest height in lawn
        """
        # print "\ntry to remove cols and rows with {0} from lawn {1}".format(self.lowest_h, self.lawn)
        for row, col in self.get_lowest_place(self.lowest_h):
            row_with_elem = self.get_row(row)
            # print "checking elem {0} in row {1}".format(self.lowest_h, row_with_elem)
            if all(x == self.lowest_h for x in row_with_elem):
                # print "deleting row {0}: {1}".format(row, row_with_elem)
                # delete row
                self.del_row(row)
                # print "new lawn: {0}".format(self.lawn)
                # print "new heights: {0}".format(self.heights)
                # print "new available_heights: {0}".format(self.available_heights)
                # print "new lowest_h: {0}".format(self.lowest_h)
                return True
            col_with_elem = self.get_col(col)
            # print "checking elem {0} in col {1}".format(self.lowest_h, col_with_elem)
            if all(x == self.lowest_h for x in col_with_elem):
                # print "deleting col {0}: {1}".format(col, col_with_elem)
                # delete col
                self.del_col(col)
                # print "new lawn: {0}".format(self.lawn)
                # print "new heights: {0}".format(self.heights)
                # print "new available_heights: {0}".format(self.available_heights)
                # print "new lowest_h: {0}".format(self.lowest_h)
                return True
        return False


def main():
    t = int(raw_input())
    result = []
    s = Solver()
    for tc in xrange(1, t+1):
        res = s.solve_case()
        res = 'YES' if res else 'NO'
        result.append('Case #{0}: {1}'.format(tc, res))
        # print "====================\n\n"

    print "\n".join(result)

if __name__ == '__main__':
    main()
