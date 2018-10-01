#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solver(object):
    def __init__(self, case, fhi, fho):
        # line 1 of the test -> 1st row containing card.
        a1 = int(fhi.readline(), 10)
        arr1 = set([map(int, fhi.readline().split()) for i in range(4)][a1 - 1])
        a2 = int(fhi.readline(), 10)
        arr2 = set([map(int, fhi.readline().split()) for i in range(4)][a2 - 1])
        possible = arr1 & arr2
        if len(possible) == 0:
            fho.write('Case #%d: Volunteer cheated!\n' % case)
        elif len(possible) == 1:
            fho.write('Case #%d: %d\n' % (case, possible.pop()))
        else:
            fho.write('Case #%d: Bad magician!\n' % case)

if __name__ == '__main__':
    with open('a-small-in') as fhi, open('a-small-out', 'w') as fho:
        for case in range(int(fhi.readline())):
            Solver(case + 1, fhi, fho)
