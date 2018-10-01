import re
import sys


EXAMPLE_IN = """6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O

"""

EXAMPLE_OUT = """Case #1: X won
Case #2: Draw
Case #3: Game has not completed
Case #4: O won
Case #5: O won
Case #6: O won
"""

def status(case):
    rows = case
    cols = map("".join, zip(*case))
    diags = ["".join(case[i][abs(j-i)]
                     for i in range(4))
             for j in [0, 3]]
    possibilities = "\n".join(rows + cols + diags)
    ## print 'pos, ', possibilities
    for mark in 'XO':
        if re.search('^[%sT]{4}$' % mark, possibilities, re.MULTILINE):
            return mark + ' won'
    if '.' in possibilities:
        return "Game has not completed"
    return "Draw"

def main(s):
    cases = [case.split('\n')
             for case in s.strip().split('\n', 1)[1].split('\n\n')]
    for i, case in enumerate(cases):
        print 'Case #%d: %s' % (i+1, status(case))

#    test_cases = [lines[i*4for i in range(cases)]


if __name__ == '__main__':
    if len(sys.argv) == 1:
        input = EXAMPLE_IN
    else:
        input = open(sys.argv[1]).read()

    main(input)
