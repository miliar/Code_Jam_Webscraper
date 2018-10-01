#!/usr/bin/python

"""
Author: Morten Lied Johansen - mortenjo@ifi.uio.no

Google CodeJam 2010
Round: 1C
Problem: C
"""

import os
import sys
import time
from cStringIO import StringIO
import unittest
import logging
from logging import info, debug, error

# Set up basic logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

def yield_line_of_items(reader):
    for x in reader.readline().strip().split():
        yield x

def read_line_of_items(reader):
    return list(yield_line_of_items(reader))

def yield_line_of_ints(reader):
    for i in yield_line_of_items(reader):
        yield int(i)

def read_line_of_ints(reader):
    return list(yield_line_of_ints(reader))

def yield_lines_of_items(reader, num=1):
    for i in range(num):
        yield read_line_of_items(reader)

def read_lines_of_items(reader, num=1):
    return list(yield_lines_of_ints(reader, num))

def yield_lines_of_ints(reader, num=1):
    for i in range(num):
        yield read_line_of_ints(reader)

def read_lines_of_ints(reader, num=1):
    return list(yield_lines_of_ints(reader, num))

class Solver(object):
    def __init__(self, input_name):
        self.input_name = input_name
        self.output_name = self._make_output_name()

    def _make_output_name(self):
        basename, ext = os.path.splitext(self.input_name)
        output_name = basename + ".out"
        return output_name

    def open_output(self):
        return open(self.output_name, "w")

    def open_input(self):
        return open(self.input_name, "r")

    def main(self):
        input = self.open_input()
        output = self.open_output()
        self.solve(input, output)

    def solve(self, input, output):
        number_of_cases = read_line_of_ints(input)[0]
        for casenr in xrange(number_of_cases):
            info("Solving case %d" % (casenr + 1))
            result = self.solve_case(*self.read_case_input(input))
            info("Result: %s", result)
            output.write("Case #%d: %s\n" % (casenr + 1, result))
            output.flush()

    def read_case_input(self, input):
        m, n = read_line_of_ints(input)
        rows = list()
        for i in range(m):
            line = input.readline().strip()
            bstr = bin(int(line, 16))
            blist = list(bstr[2:])
            if len(blist) < n:
                for i in range(n-len(blist)):
                    blist.insert(0, "0")
            rows.append(blist)
        return rows, m, n

    def solve_case(self, rows, m, n):
        counter = dict()
        debug("Solving for bark of size (%d, %d)", m,n)
        print_board(rows)
        for size in range(n,0,-1):
            debug("Trying for size %d", size)
            counter[size] = 0
            for row in range(m):
                if row+size > m:
                    break
                for col in range(n):
                    if col+size > n:
                        break
                    v = View(rows, col, row, size)
                    debug("Board of size %d created at (%d,%d)", size, col, row)
                    if v.is_chessboard():
                        v.mark()
                        counter[size] += 1
                        print_board(rows)
        results = sorted([(key, value) for key, value in counter.iteritems() if value > 0])
        results.reverse()
        text = list()
        text.append("%d" % len(results))
        for key, value in results:
            text.append("%d %d" % (key, value))
        return "\n".join(text)

def print_board(rows):
    root_logger = logging.getLogger()
    if root_logger.isEnabledFor(logging.DEBUG):
        debug("*"*len(rows))
        for r in rows:
            line = list()
            for square in r:
                line.append(square)
            debug("".join(line))
        debug("*" * len(rows))

def get_checkered_row(length):
    row = "10"*(length/2)
    if length % 2 == 1:
        return list(row + "1")
    return list(row)

def rotate(row):
    last = row.pop()
    if row[0] == "0":
        row.insert(0, "1")
    else:
        row.insert(0, "0")

class View(object):
    def __init__(self, rows, x, y, size):
        self.rows = rows
        self.x = x
        self.y = y
        self.size = size

    def mark(self):
        for y in range(self.size):
            for x in range(self.size):
                self.rows[self.y + y][self.x + x] = " "

    def is_chessboard(self):
        self.print_view()
        if self.size == 1:
            row = self.get_row(0)
            return row[0] != " "
        chessrow = get_checkered_row(self.size)
        first = True
        y = 0
        while y < self.size:
            myrow = self.get_row(y)
            if first:
                if myrow[0] == "0":
                    rotate(chessrow)
                first = False
            if chessrow != myrow:
                if self.size == 4:
                    debug("y: %d, myrow: %r, chessrow: %r", y, myrow, chessrow)
                return False
            rotate(chessrow)
            y += 1
        debug("Is a chessboard")
        return True

    def print_view(self):
        if self.size != 4:
            return
        debug("** View **")
        rows = list()
        for y in range(self.size):
            rows.append(self.get_row(y))
        print_board(rows)

    def get_row(self, y):
        return self.rows[self.y+y][self.x:self.x+self.size]

# === Verify correctness of sample data
class SampleTester(unittest.TestCase):
    def setUp(self):
        self.data = open("sample.correct", "r").read()
    def test_sample(self):
        output = StringIO()
        solver = Solver("sample.in")
        input = solver.open_input()
        solver.solve(input, output)
        self.assertEqual(self.data, output.getvalue())

if __name__ == "__main__":
    if "--debug" in sys.argv:
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
    input_name = sys.argv[1]
    if input_name == "test":
        suite = unittest.TestLoader().loadTestsFromTestCase(SampleTester)
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        start = time.time()
        solver = Solver(input_name)
        solver.main()
        end = time.time()
        print "Time spent: %s" % time.strftime("%M minutes, %S seconds", time.gmtime(end-start))
