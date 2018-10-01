from __future__ import division
import sys
sys.setrecursionlimit(10000)
# cookie clicker
EXAMPLE_IN = """\
3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16"""

EXAMPLE_OUT = """\
Case #1: 7
Case #2: Bad magician!
Case #3: Volunteer cheated!
"""


def solve(first_ans, first_cards, second_ans, second_cards):
    first_possible = set(first_cards[first_ans-1])
    second_possible = set(second_cards[second_ans-1])
    sols = first_possible & second_possible
    if len(sols) == 1:
        return list(sols)[0]
    elif not sols:
        return "Volunteer cheated!"
    return 'Bad magician!'



def main(lines):
    for i in xrange(int(next(lines))):
        first_ans = int(next(lines))
        first_cards = [map(int, next(lines).split()) for _ in range(4)]
        second_ans = int(next(lines))
        second_cards = [map(int, next(lines).split()) for _ in range(4)]
        ans = 'Case #%d: %s' % (i+1, solve(first_ans, first_cards, second_ans, second_cards))
        print ans




if __name__ == '__main__':
    if len(sys.argv) == 1:
        input = iter(EXAMPLE_IN.split('\n'))
    else:
        input = open(sys.argv[1])
    main(input)
