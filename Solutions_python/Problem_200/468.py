#!/usr/bin/env python3

"""
Google Code Jam
Qualification Round 2017
Problem B.
"""

import argparse

def num_digits(n):
    return len(str(n))

class TestCase:
    def __init__(self, N):
        self.N = N
    def is_tidy(self):
        return sorted(str(self.N)) == [x for x in str(self.N)]
    def solve(self):
        while not self.is_tidy():
            k = 0
            for k in range(num_digits(self.N) - 1):
                if str(self.N)[k] > str(self.N)[k + 1]:
                    self.N -= self.N % (10 ** (num_digits(self.N) - k - 1)) + 1
                    break
        return self.N

def read_data(filename):
    """Read and parse the input data"""
    with open(filename) as _file:
        test_cases = []
        num_test_cases = int(_file.readline())
        for _ in range(num_test_cases):
            N = int(_file.readline())
            test_cases.append(TestCase(N))
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
