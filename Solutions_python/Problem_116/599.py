# task = 'A-sample'
# task = 'A-small-attempt0'
task = 'A-large'


testCaseSpec = '''
$l1
$l2
$l3
$l4
$emptyLine
'''

x = 'X'
o = 'O'
empty = '.'
t = 'T'

xWon = 'X won'
oWon = 'O won'
draw = 'Draw'
incomplete = 'Game has not completed'

def solve(l1, l2, l3, l4, emptyLine):

    # rows
    rows = [l1, l2, l3, l4]
    cols = list(zip(l1, l2, l3, l4))
    diag = [l1[0]+l2[1]+l3[2]+l4[3], l1[3]+l2[2]+l3[1]+l4[0]]

    lines = rows + cols + diag
    for line in lines:
        if all(x == field or t == field for field in line):
            return xWon
        if all(o == field or t == field for field in line):
            return oWon

    for line in lines:
        if empty in line:
            return incomplete

    return draw


from template import Solver

Solver(task, testCaseSpec, solve).solve()
