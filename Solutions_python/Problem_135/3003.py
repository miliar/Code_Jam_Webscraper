import sys

def rline(f=str):
    return f(sys.stdin.readline())

def sline(f=str):
    return [ f(elem) for elem in rline().split(' ') ]

def test(row1, row2):
    inter = row1 & row2
    if len(inter) == 0:
        return 'Volunteer cheated!'
    if len(inter) > 1:
        return 'Bad magician!'
    for elem in inter:
        return str(elem)

def readSelectedRow():
    selectedRow = rline(int)
    for rowNo in range(4):
        line = set(sline(int))
        if rowNo + 1 == selectedRow:
            row = line
    return row

nbTest = rline(int)
for testNo in range(nbTest):
    row1 = readSelectedRow()
    row2 = readSelectedRow()
    res = test(row1, row2)
    print('Case #%d: %s' % (testNo + 1, res))
