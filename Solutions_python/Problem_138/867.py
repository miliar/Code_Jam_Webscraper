#!/usr/bin/env python

import sys

def play_deceitful_war(nblocks, kblocks):
    for b in nblocks:
        if b > kblocks[0]:
            kblocks.remove(kblocks[0])

    return len(nblocks) - len(kblocks)

def play_war(nblocks, kblocks):
    nblocks.reverse()
    kblocks.reverse()

    i = 0
    for b in nblocks:
        if b > kblocks[i]:
            kblocks = kblocks[:-1]
        else:
            i += 1

    return len(nblocks) - len(kblocks)

def solve_case(case_num):
    number_of_blocks = sys.stdin.readline()
    naomi_blocks = [float(x.strip()) for x in sys.stdin.readline().split(' ')]
    naomi_blocks.sort()

    ken_blocks = [float(x.strip()) for x in sys.stdin.readline().split(' ')]
    ken_blocks.sort()

    dwins = play_deceitful_war(naomi_blocks[:], ken_blocks[:])
    wins = play_war(naomi_blocks[:], ken_blocks[:])

    print "Case #%s: %s %s" % (case_num, dwins, wins)

def main():
    test_cases = sys.stdin.readline()
    cases_solved = 0

    while cases_solved < test_cases:
        cases_solved += 1
        solve_case(cases_solved)

if __name__ == '__main__':
    main()
