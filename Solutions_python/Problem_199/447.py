#!/usr/bin/env python3

"""
Google Code Jam
Qualification Round 2017
Problem A.
"""

import argparse

class TestCase:
    def __init__(self, row, K):
        self.row = row
        self.K = K
    def flip(self, start):
        for i in range(start, start + self.K):
            self.row[i] = 1 - self.row[i]
    def solve(self):
        flips = 0
        for i in range(len(self.row) - self.K + 1):
            if self.row[i] == 0:
                self.flip(i)
                flips += 1
        for i in range(len(self.row)):
            if self.row[i] == 0:
                return "IMPOSSIBLE"
        return flips

def read_data(filename):
    """Read and parse the input data"""
    with open(filename) as _file:
        test_cases = []
        num_test_cases = int(_file.readline())
        for _ in range(num_test_cases):
            row, K = [x for x in _file.readline().split()]
            K = int(K)
            row = [0 if x == "-" else 1 for x in row]
            test_cases.append(TestCase(row, K))
    return num_test_cases, test_cases

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("problem", help="problem to solve")
    PARSER.add_argument("--out", help="output result to file", action="store_true")
    ARGS = PARSER.parse_args()
    NUM_TEST_CASES, TEST_CASES = read_data(ARGS.problem + ".in")
    if ARGS.out:
        OUTPUT_FILE = open(ARGS.problem + ".out", 'w')
    for it in range(NUM_TEST_CASES):
        test_case = TEST_CASES[it]
        result = "Case #{}: {}".format(it + 1, test_case.solve())
        if ARGS.out:
            print(result, file=OUTPUT_FILE)
        else:
            print(result)
    if ARGS.out:
        OUTPUT_FILE.close()
