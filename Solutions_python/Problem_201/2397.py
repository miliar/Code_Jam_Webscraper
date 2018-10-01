import os, sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), '.'))
from core import *

# -----------------------------------------------------------------------------
# Round Q 2017
# Problem A. Oversized Pancake Flipper
# + (which represents a pancake that is initially happy side up)
# - (which represents a pancake that is initially blank side up).
# -----------------------------------------------------------------------------
def flip(pancakes, start, end):
    for index in xrange(start, end):
        if pancakes[index] == '+': pancakes[index] = '-'
        elif pancakes[index] == '-': pancakes[index] = '+'


def is_valid(pancakes):
    for state in pancakes:
        if pancakes[0] != state:
            return False
    return True


class PancakeFlipper(Solution):
    def handle(self, case):
        pancakes, flipper_size = case.case_input.split(' ')
        pancakes = [c for c in pancakes]
        flipper_size = int(flipper_size)

        flips = 0
        i = 0
        while (i + flipper_size) <= len(pancakes):
            if pancakes[i] != '+':
                flip(pancakes, i, i+flipper_size)
                flips += 1
            i += 1

        out = str(flips) if is_valid(pancakes) else 'IMPOSSIBLE'
        case.register_case_output(out)

    def case_samples(self):
        return [
            '---+-++- 3',
            '+++++ 4',
            '-+-+- 4',
        ]

    def case_files(self):
        return [
            '../data/2017-google-code-jam/round-q/A-small-attempt0.in',
            '../data/2017-google-code-jam/round-q/A-large.in',
        ]


# -----------------------------------------------------------------------------
# Round Q 2017
# Problem B. Tidy Numbers
# -----------------------------------------------------------------------------
class TidyNumbers(Solution):
    def handle(self, case):
        number = [int(digit) for digit in case.case_input]

        non_tidy_index = self.find_non_tidy_index(number)
        tidy_number = number if non_tidy_index == -1 else self.convert_to_tidy(number, non_tidy_index)

        out = str(int(''.join([str(digit) for digit in tidy_number])))
        case.register_case_output(out)

    def convert_to_tidy(self, candidate, non_tidy_index):
        number = candidate[:]
        number[non_tidy_index] -= 1
        for index in xrange(non_tidy_index + 1, len(number)):
            number[index] = 9
        return number

    def find_non_tidy_index(self, number):
        tidy_index = 0
        pivot = -1
        for index, digit in enumerate(number):
            if digit < pivot:
                return tidy_index
            if pivot != digit:
                tidy_index = index
            pivot = digit
        return -1

    def case_samples(self):
        return [
            '132',
            '1000',
            '7',
            '111111111111111110',
            '129',
            '109',
        ]

    def case_files(self):
        return [
            '../data/2017-google-code-jam/round-q/B-small-attempt0.in',
            '../data/2017-google-code-jam/round-q/B-large.in',
        ]


# -----------------------------------------------------------------------------
# Round Q 2017
# Problem C. Bathroom Stalls
# -----------------------------------------------------------------------------
class StallState(object):
    def __init__(self, index, occupied=False, ls=0, rs=0):
        self.index = index
        self.occupied = occupied
        self.ls = ls
        self.rs = rs

    def min_lsrs(self):
        return min(self.ls, self.rs)

    def max_lsrs(self):
        return max(self.ls, self.rs)

    def __repr__(self):
        return '%s: { occupied=%s, ls=%s, rs=%s }' % (self.index, self.occupied, self.ls, self.rs)


class BathroomStalls(Solution):
    def handle(self, case):
        n_stalls, n_persons = [int(n) for n in case.case_input.split(' ')]
        stalls = [StallState(index=index, ls=index, rs=n_stalls - index - 1) for index in xrange(n_stalls)]

        chosen_stall = None
        for _ in xrange(n_persons):
            chosen_stall = self.choose_stall(stalls)
            self.place_person(chosen_stall, stalls)

        out = '%s %s' % (chosen_stall.max_lsrs(), chosen_stall.min_lsrs())
        case.register_case_output(out)
        # print out

    def choose_stall(self, stalls):
        min_lsrs = {}
        for stall in stalls:
            if stall.occupied: continue
            min_lsrs.setdefault(stall.min_lsrs(), [])
            min_lsrs[stall.min_lsrs()].append(stall)

        max_lsrs = {}
        for min_stall in min_lsrs[max(min_lsrs.keys())]:
            max_lsrs.setdefault(min_stall.max_lsrs(), [])
            max_lsrs[min_stall.max_lsrs()].append(min_stall)

        min_index = len(stalls)
        chosen_stall = None
        for indexed_stall in max_lsrs[max(max_lsrs.keys())]:
            if indexed_stall.index < min_index:
                chosen_stall = indexed_stall
                min_index = indexed_stall.index

        return chosen_stall

    def place_person(self, chosen_stall, stalls):
        chosen_stall.occupied = True

        rs = 0
        is_previous_rs_occupied = True
        for index in reversed(xrange(chosen_stall.index)):
            if is_previous_rs_occupied: rs = 0
            stalls[index].rs = rs
            rs += 1
            is_previous_rs_occupied = stalls[index].occupied

        ls = 0
        is_previous_ls_occupied = True
        for index in xrange(chosen_stall.index + 1, len(stalls)):
            if is_previous_ls_occupied: ls = 0
            stalls[index].ls = ls
            ls += 1
            is_previous_ls_occupied = stalls[index].occupied

    def case_samples(self):
        return [
            '4 2',
            '5 2',
            '6 2',
            '1000 1000',
            '1000 1',
        ]

    def case_files(self):
        return [
            # '../data/2017-google-code-jam/round-q/C-small-1-attempt0.in',
            '../data/2017-google-code-jam/round-q/C-small-1-attempt1.in',
            # '../data/2017-google-code-jam/round-q/C-small-2-attempt0.in',
            '../data/2017-google-code-jam/round-q/C-large.in',
        ]


run(__name__)
