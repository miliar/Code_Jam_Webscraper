#!/usr/bin/env python3
"""
Standing Ovation problem
for Google Code Jam 2015
Qualification Round

Link to problem description:
https://code.google.com/codejam/contest/6224486/dashboard#s=p0

Author: 
  Chris Nitsas
  (nitsas)

Language:
  Python 3(.4)

Date:
  April, 2015

Usage:
  python3 runme.py input_file
"""


import sys
import argparse
import collections
# modules I've written:
from helpful import *


_program_description = \
'''TEMPLATE PROGRAM DESCRIPTION'''


_input_file_description = \
'''TEMPLATE INPUT FILE DESCRIPTION'''


"""
smax -- an int; the maximum shyness level of the shyest person
people_per_level -- a tuple of int; the kth element represents the number of
                    people who have shyness level k
"""
TestCase = collections.namedtuple('TestCase', ['smax', 'people_per_level'])


def parse_args():
    """
    Parse the command line arguments and return them in a namespace.
    """
    parser = argparse.ArgumentParser(description=_program_description)
    parser.add_argument('input_file', help=_input_file_description)
    #parser.add_argument('-v', '--verbose', action='store_true', 
    #                    default=False, help='show progress')
    args = parser.parse_args()
    return args


def min_num_friends_for_ovation(test_case):
    num_less_shy_people = 0
    max_disparity = 0
    for k, num_people_who_are_k_shy in enumerate(test_case.people_per_level):
        if num_less_shy_people < k:
            disparity = k - num_less_shy_people
            if disparity > max_disparity:
                max_disparity = disparity
        num_less_shy_people += num_people_who_are_k_shy
    return max_disparity


def main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        T = read_int(f)
        def digitstring_to_tuple_of_int(digitstring):
            return tuple(map(int, digitstring))
        test_cases = list()
        for i in range(T):
            tc = TestCase(*read_list_of_types(f, 
                                         [int, digitstring_to_tuple_of_int]))
            test_cases.append(tc)
    for i, tc in enumerate(test_cases, start=1):
        print('Case #{}: {}'.format(i, min_num_friends_for_ovation(tc)))
    return 0


if __name__ == "__main__":
    status = main(parse_args().input_file)
    sys.exit(status)
