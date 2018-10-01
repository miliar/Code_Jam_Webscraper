#!/usr/bin/env python3
from queue import Queue


def read_cases():
    case_count = input()
    cases = []
    for x in range(int(case_count)):
        raw = input().split()
        destination = int(raw[0])
        horses_count = int(raw[1])
        horses = list()

        for h in range(horses_count):
            raw2 = input().split()
            horses.append({
                'position': int(raw2[0]),
                'speed': int(raw2[1])
            })

        cases.append({
            'destination': destination,
            'horses': horses,
        })
    return cases


class Solver:

    def __init__(self, case):
        self.case = case
        self.d = case['destination']

    def solve(self):
        time = self.get_biggest_time()
        return self.d / time

    def get_biggest_time(self):
        def keyfunc(x):
            remains = self.d - x['position']
            remains = 0 if remains < 0 else remains
            time = remains / x['speed']
            return time
        return max([keyfunc(x) for x in self.case['horses']])


def main():
    cases = read_cases()
    for i, case in enumerate(cases):
        s = Solver(case)
        result = s.solve()
        print("Case #{}: {}".format(i + 1, result))

if __name__ == '__main__':
    main()
