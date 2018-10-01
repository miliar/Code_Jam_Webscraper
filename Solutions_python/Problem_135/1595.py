from __future__ import print_function
import sys


def read_input(f):
    T = int(f.readline().strip())

    for i in xrange(T):
        output = {}
        output['ans1'] = int(f.readline().strip())
        output['cards1'] = [f.readline().strip().split(" ") for j in xrange(4)]
        output['ans2'] = int(f.readline().strip())
        output['cards2'] = [f.readline().strip().split(" ") for j in xrange(4)]
        yield output


def check_case(case):
    first_row = case['cards1'][case['ans1'] - 1]
    second_row = case['cards2'][case['ans2'] - 1]
    matches = [card for card in first_row if card in second_row]
    if len(matches) == 1:
        result = matches[0]
    elif len(matches) == 0:
        result = "Volunteer cheated!"
    else:
        result = "Bad magician!"
    return result


if __name__ == "__main__":
    input_filename = sys.argv[1]
    with open(input_filename) as input_file:
        case_no = 0
        for case in read_input(input_file):
            case_no += 1
            # check_case(case)
            print("Case #" + str(case_no) + ": " + check_case(case))
