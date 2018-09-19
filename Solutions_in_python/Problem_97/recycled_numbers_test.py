import googlers
import recycled_numbers

__author__ = 'dmorgant'

import unittest

input = "4\n\
1 9\n\
10 40\n\
100 500\n\
1111 2222"

output = "Case #1: 0\n\
Case #2: 3\n\
Case #3: 156\n\
Case #4: 287"

class GooglersTest(unittest.TestCase):
    def test_input_output(self):
        self.assertEqual(output, recycled_numbers.process(input))

    def test_case_1(self):
        solver = recycled_numbers.Solver(1, 9)
        self.assertEqual(solver.solve(), 0)

    def test_case_2(self):
        solver = recycled_numbers.Solver(10, 40)
        self.assertEqual(solver.solve(), 3)

    def test_case_3(self):
        solver = recycled_numbers.Solver(100, 500)
        self.assertEqual(solver.solve(), 156)

    def test_case_4(self):
        solver = recycled_numbers.Solver(1111, 2222)
        self.assertEqual(solver.solve(), 287)

    def xtest_case_huge(self):
        solver = recycled_numbers.Solver(1000000, 9999999)
        self.assertEqual(solver.solve(), -1)

if __name__ == '__main__':
    unittest.main()
