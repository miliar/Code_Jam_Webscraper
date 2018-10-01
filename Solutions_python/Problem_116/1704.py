# -*- coding: utf-8 -*-

from sys import exit, stdin
from pprint import PrettyPrinter
from itertools import chain


def check_for_letter(line, letter):
    count = line.count(letter)
    t_is_present = 'T' in line

    if (count == 4) or (t_is_present and count == 3):
        return True

    return False


def check_group(group):
    horizontals = group[:]
    verticals = [
        ''.join([line[column] for line in group])
        for column in range(len(group))
    ]
    diagonals = [
        ''.join([group[x][x] for x in range(len(group))]),
        ''.join([group[x][len(group) - x - 1] for x in range(len(group))])
    ]

    for line in chain(horizontals, verticals, diagonals):
        if check_for_letter(line, 'X'):
            return 'X won'

        if check_for_letter(line, 'O'):
            return 'O won'

    if '.' in ''.join(group):
        return 'Game has not completed'

    return 'Draw'


if __name__ == '__main__':
    p = PrettyPrinter()

    T = int(stdin.readline())

    for index in range(T):
        group = [
            stdin.readline().strip()
            for _ in range(4)
        ]
        stdin.readline()

        print 'Case #%d: %s' % (index + 1, check_group(group))

    exit()
