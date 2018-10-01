#!/usr/bin/env python
"""
Problem A. Magic Trick
"""
if __name__ == "__main__":
    num_of_cases = int(raw_input())
    for case in range(num_of_cases):
        first_row = int(raw_input())
        for i in range(1, 5):
            line = raw_input()
            if i == first_row:
                first_row = line.split()

        second_row = int(raw_input())
        for i in range(1, 5):
            line = raw_input()
            if i == second_row:
                second_row = line.split()

        result_set = set(first_row) & set(second_row)
        msg = ""
        if len(result_set) == 1:
            msg = result_set.pop()
        elif len(result_set) == 0:
            msg = "Volunteer cheated!"
        else:
            msg = "Bad magician!"
        print "Case #{0}: {1}".format(case + 1, msg)
