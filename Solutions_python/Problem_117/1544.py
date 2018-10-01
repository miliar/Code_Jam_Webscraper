# -*- coding: utf-8 -*-
# Google Code Jam 2013 - Qualification Round - Lawnmower
# http://code.google.com/codejam/contest/2270488/dashboard#s=p1
# © 2013 Aluísio Augusto Silva Gonçalves
# This Source Code Form is subject to the terms of the Mozilla Public License,
# version 2.0.  If a copy of the MPL was not distributed with this file, You
# can obtain one at http://mozilla.org/MPL/2.0/.


# Problem description {{{1
##########################

"""
   Lawnmower

"""


# Imports {{{1
##############

from __future__ import division, unicode_literals

import CodeJam

if not CodeJam.Py3k:
    range = xrange


# Test case {{{1
################

class TestCase(CodeJam.TestCase):
    """ Custom test case for the Lawnmower problem. """

    @classmethod
    def parseInput (cls, file):
        """ Get the test cases for the Lawnmower problem. """
        nr_tests, tests = int(file.readline()), []
        for i in range(1, nr_tests + 1):
            test = CodeJam.TestCase(i)
            n, m = [int(s) for s in file.readline().split()]
            test.input = ((n, m), [])
            for i in range(n):
                test.input[1].append(file.readline().rstrip('\n'))
            tests.append(test)
        return tests


# Entry point {{{1
##################

@CodeJam.ProblemSolver(__name__, TestCase)
def solve (input):
    n, m = input[0]
    grid = [int(sq) for r in input[1] for sq in r.split()]
    base_height = max(grid)
    for i, h in enumerate(grid):
        if h == base_height:
            continue
        # Check for a line or column with this height
        chead = i % m
        column = [grid[j] for j in range(chead, len(grid) - (m - chead) + 1, m)]
        lhead = i - chead
        line = [grid[j] for j in range(lhead, lhead + m)]
        if (column.count(h) != len(column)) and (line.count(h) != len(line)):
            return 'NO'
    return 'YES'
