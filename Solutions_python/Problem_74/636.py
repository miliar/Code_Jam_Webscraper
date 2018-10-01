#!/usr/bin/python

"""
Author: Morten Lied Johansen - mortenjo@ifi.uio.no

Google CodeJam 2011
Round: Qualifier
Problem: Bot Trust
"""

import os
import sys
import time
from pprint import pformat
from cStringIO import StringIO
import unittest
import logging
from logging import info, debug, error
from multiprocessing import Pool

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

def run_in_process(case_solver):
    return case_solver.solve()

class Command(object):
    def __init__(self, bot, button):
        self.bot = bot
        self.button = button

class Solver(object):
    def __init__(self, input_name, use_mp=False):
        self.input_name = input_name
        self.output_name = self._make_output_name()
        self.use_mp = use_mp

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
        solvers = list()
        for casenr in xrange(number_of_cases):
            solvers.append(CaseSolver(casenr+1, self.read_case_input(input)))
        if self.use_mp:
            p = Pool()
            solutions = p.map(run_in_process, solvers)
        else:
            solutions = map(run_in_process, solvers)
        for casenr, result in sorted(solutions):
            output.write("Case #%d: %s\n" % (casenr, result))
            output.flush()

    def read_case_input(self, input):
        commands = list()
        iterator = yield_line_of_items(input)
        number_of_commands = int(iterator.next())
        for i in range(number_of_commands):
            bot = iterator.next()
            button = int(iterator.next())
            commands.append(Command(bot, button))
        return commands

class Position(object):
    def __init__(self):
        self.time = 0
        self.location = 1

    def update(self, other):
        self.time = other.time
        self.location = other.location

class Bot(object):
    def __init__(self, name, common_position):
        self.name = name
        self.position = Position()
        self.common_position = common_position

    def move(self, new_location):
        time_to_move = abs(self.position.location - new_location)
        self.position.time += time_to_move
        self.position.location = new_location
        debug("[%-6s] Move to button %d in %d seconds (completed: %d)", self.name, self.position.location, time_to_move, self.position.time)

    def push_button(self):
        self.position.time += 1
        debug("[%-6s] Push button %d (completed: %d)", self.name, self.position.location, self.position.time)

    def execute_next_step(self, new_location):
        self.move(new_location)
        new_time = max(self.position.time, self.common_position.time)
        self.position.time = new_time
        self.push_button()
        self.common_position.update(self.position)

class CaseSolver(object):
    def __init__(self, casenr, commands):
        self.casenr = casenr
        self.commands = commands

    def solve(self):
        info("Solving case %d", self.casenr)
        common_position = Position()
        bots = {
            "O": Bot("0range", common_position),
            "B": Bot("Blue", common_position)
        }
        for command in self.commands:
            bot = bots[command.bot]
            bot.execute_next_step(command.button)
        debug("Result: %s", common_position.time)
        return self.casenr, common_position.time

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
    use_mp = False
    if "--use-mp" in sys.argv:
        use_mp = True
    input_name = sys.argv[1]
    if input_name == "test":
        suite = unittest.TestLoader().loadTestsFromTestCase(SampleTester)
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        start = time.time()
        solver = Solver(input_name, use_mp)
        solver.main()
        end = time.time()
        info("Time spent: %s" % time.strftime("%M minutes, %S seconds", time.gmtime(end-start)))
