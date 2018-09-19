# -*- coding: utf-8 -*-
__author__ = 'Lauri Elias'

with open('input.txt') as f:
    content = f.readlines()

out = open('output.txt', 'w')
for case, line in enumerate(content[1:]):
    X, R, C = map(int, line.split())

    gabriel_wins = True

    if X >= 7:
        gabriel_wins = False
    elif X > R and X > C:
        gabriel_wins = False
    elif (R * C) % X != 0:
        gabriel_wins = False
    elif min(R, C) < (X + 1) // 2:
        gabriel_wins = False
    elif X in (1, 2, 3):
        gabriel_wins = True
    elif X == 4:
        gabriel_wins = min(R, C) > 2
    elif X == 5:
        gabriel_wins = (max(R, C) == 5) and not(min(R, C) == 3)
    elif X == 6:
        gabriel_wins = min(R, C) > 3

    if gabriel_wins:
        out.write('Case #%d: GABRIEL\n' % (case + 1))
    else:
        out.write('Case #%d: RICHARD\n' % (case + 1))
out.close()
