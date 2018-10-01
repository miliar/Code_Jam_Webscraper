#!/usr/bin/python
import sys, string


def flip(pancakes, index, flipper_size):
    for i in range(flipper_size):
        pancakes[index + i] = '+' if pancakes[index + i] == '-' else '-'


def solve(pancakes, flipper_size, case_number):
    count = 0
    index = 0
    while True:
        if len(pancakes) - index < flipper_size:
            break

        if pancakes[index] == '+':
            index += 1
            continue

        flip(pancakes, index, flipper_size)
        count += 1
        index += 1

    if '-' in pancakes:
        print("Case #%d: IMPOSSIBLE" % case_number)
        return

    print("Case #%d: %d" % (case_number, count))


def main():
    r = sys.stdin
    if len(sys.argv) > 1:
        r = open(sys.argv[1], 'r')

    total_cases = r.readline()
    for case_number in range(1, int(total_cases) + 1):
        pancakes, flipper_size = r.readline().strip().split(' ')

        solve(list(pancakes), int(flipper_size), case_number)


if __name__ == "__main__":
    main()
