import googlers

__author__ = 'dmorgant'

import unittest

input = "4\n\
3 1 5 15 13 11\n\
3 0 8 23 22 21\n\
2 1 1 8 0\n\
6 2 8 29 20 8 18 18 21"

output = "Case #1: 3\n\
Case #2: 2\n\
Case #3: 1\n\
Case #4: 3"

class GooglersTest(unittest.TestCase):
    def test_input_output(self):
        self.assertEqual(output, googlers.process(input))

    def test_sample(self):
        solver = googlers.Solver(2, 8, [29, 20, 8, 18, 18, 21])
        self.assertEqual(solver.solve(), 3)

    def test_case_2(self):
        solver = googlers.Solver(0, 8, [23, 22, 21])
        self.assertEqual(solver.solve(), 2)

    def test_case_3(self):
        solver = googlers.Solver(1, 1, [8, 0])
        self.assertEqual(solver.solve(), 1)

    def test_lower_bounds(self):
        solver = googlers.Solver(1, 1, [8, 1])
        self.assertEqual(solver.solve(), 2)

if __name__ == '__main__':
    unittest.main()
