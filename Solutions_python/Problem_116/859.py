#!/usr/bin/env python
import fileinput
def getlines():
    inp = fileinput.input()
    for line in inp:
        yield line.rstrip()

getline = getlines()
cases = int(getline.next())

def lines_from_horizontal(rows):
    lines = []
    lines += rows
    for i in range(4):
        lines.append("".join([rows[x][i] for x in range(4)]))
    lines.append("".join([rows[x][x] for x in range(4)]))
    lines.append("".join([rows[3-x][x] for x in range(4)]))
    return lines

for case in range(cases):
    has_dots = False
    winner = None
    rows = [getline.next() for x in range(4)]
    all_lines = lines_from_horizontal(rows)
    for line in all_lines:
        if '.' in line:
            has_dots = True
        else:
            if 'O' not in line:
                winner = 'X'
            elif 'X' not in line:
                winner = 'O'
    result = ""
    if winner:
        result = "%s won" % winner
    elif has_dots:
        result = "Game has not completed"
    else:
        result = "Draw"
    print("Case #%d: %s" % (case + 1, result))

    getline.next()
