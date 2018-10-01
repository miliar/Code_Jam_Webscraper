#!/usr/bin/env python
import fileinput
import sys

sys.setrecursionlimit(1005)


def solve_deceitful(naomi, ken):
    return len(naomi) - _solve_deceitful(naomi, ken)


def _solve_deceitful(naomi, ken):
    # recursively make winning pairs
    # return #rounds won by ken
    if not ken:
        return 0
    highest_naomi = naomi[-1]
    for i, b in enumerate(reversed(ken)):
        if highest_naomi > b:
            # winning pair
            return i + _solve_deceitful(naomi[:-1], ken[:-1 - i])
    # naomi cannot win any anymore
    return len(ken)


def solve_regular(naomi, ken):
    # naomi picks don't matter -> go from lowest to highest
    # ken: if has higher picks lowest higher, otherwise pick lowest
    score_naomi = 0
    ken = list(ken)
    for naomi_plays in naomi:
        try:
            ken_plays = next(b for b in ken if b > naomi_plays)
        except StopIteration:
            ken_plays = ken[0]
            score_naomi += 1
        ken.remove(ken_plays)
    return score_naomi


def make_answer(case, deceitful, regular):
    return "Case #%i: %i %i" % (case, deceitful, regular)


def get_input(lines):
    nextline = lambda: next(lines)
    cases = int(nextline())
    for _ in range(cases):
        blocks = int(nextline())  # useless value
        naomi = sorted(map(float, nextline().split()))
        ken = sorted(map(float, nextline().split()))
        assert(len(naomi) == len(ken) == blocks)
        yield naomi, ken


def main():
    for i, game in enumerate(get_input(fileinput.input()), 1):
        naomi, ken = game
        print(make_answer(i, solve_deceitful(naomi, ken),
                             solve_regular(naomi, ken)))

if __name__ == '__main__':
    main()
