#!/usr/bin/env python

import sys


def read_board(fh, num_lines=4):

    board = []

    for _ in range(num_lines):
        cards = fh.readline().strip().split()
        board.extend(cards)

    return board

def parse_input(input_file):
    """Return list of cases.

    Each case is a tuple of 4 items:
        1. First answer
        2. Board (as list)
        3. Second answer
        4. Board (as list)

    """

    fh = open(input_file, 'r')
    num_cases = int(fh.readline())

    cases = []

    for _ in range(num_cases):
        case = []

        first_answer = fh.readline().strip()
        case.append(int(first_answer))

        case.append(read_board(fh))

        second_answer = fh.readline().strip()
        case.append(int(second_answer))

        case.append(read_board(fh))

        cases.append(tuple(case))

    fh.close()

    return cases

def read_row(row_num, board):
    """Return set of cards that are row row_num on board.

    The board has 4 rows of 4 cards each, and goes from
    row 1 to row 4.

    """

    start_index = (row_num - 1) * 4
    return set(board[start_index: start_index + 4])

def solve(trick):
    first_answer = trick[0]
    first_candidates = read_row(first_answer, trick[1])
    second_answer = trick[2]
    second_candidates = read_row(second_answer, trick[3])

    intersection = first_candidates & second_candidates

    if len(intersection) == 0:
        result = "Volunteer cheated!"
    elif len(intersection) == 1:
        result = str(intersection.pop())
    elif len(intersection) > 1:
        result = "Bad magician!"

    return result

def output(case_num, result):
    print "Case #%s: %s" % (case_num, result)

def main():
    if len(sys.argv) != 2:
        print "Usage: %s <input_file>" % sys.argv[0]
        sys.exit(1)

    input_file = sys.argv[1]

    tricks = parse_input(input_file)
    for case_num, trick in enumerate(tricks, 1):
        result = solve(trick)
        output(case_num, result)

if __name__ == '__main__':
    main()
