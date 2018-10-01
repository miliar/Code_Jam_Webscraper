#!/usr/bin/env python3


def read_cases():
    case_count = input()
    cases = []
    for x in range(int(case_count)):
        raw_case = input()
        cases.append(raw_case.split())
    return cases


class Solver:
    def __init__(self, last_number):
        self.last_number = int(last_number)

    def solve(self):
        rev = str(self.last_number)[::-1]
        for i, x in enumerate(rev[:-1]):
            n = rev[i + 1]
            if x < n:
                self.write_last(i)
                self.solve()
                break

    def write_last(self, i):
        s = str(self.last_number)
        the_in = len(s) - i - 1
        to_subtract = int(s[the_in:]) + 1
        # print('{} {}'.format(self.last_number, to_subtract))
        self.last_number -= to_subtract

    def result(self):
        return self.last_number


def main():
    cases = read_cases()
    for i, case in enumerate(cases):
        s = Solver(case[0])
        s.solve()
        print("Case #{}: {}".format(i + 1, s.result()))

if __name__ == '__main__':
    main()
