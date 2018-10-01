#!/usr/local/bin/python3

import sys


def nth_row(i_row):
    """Returns the n-th row of the square grid."""
    for i in range(1, i_row):
        sys.stdin.readline()

    s_row = set(sys.stdin.readline().split())

    for i in range(i_row + 1, 5):
        sys.stdin.readline()

    return s_row



i_nb_test_cases = int(sys.stdin.readline())
#print (repr(i_nb_test_cases))

for i in range(1, i_nb_test_cases + 1):
    i_first_answer = int(sys.stdin.readline())
    s_first_row  = nth_row(i_first_answer)
#    print (s_first_row)

    i_second_answer = int(sys.stdin.readline())
    s_second_row = nth_row(i_second_answer)
#    print (s_second_row)

    s_intersection = s_first_row & s_second_row
#    print (s_intersection)

    if len(s_intersection) == 1:
        print ('Case #', i ,': ', s_intersection.pop(), sep = '')
    elif len(s_intersection) == 0:
        print ('Case #', i ,': Volunteer cheated!', sep = '')
    else:
        print ('Case #', i ,': Bad magician!', sep = '')
