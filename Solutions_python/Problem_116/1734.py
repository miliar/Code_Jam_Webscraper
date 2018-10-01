# -*- coding: utf-8 -*-
# Google Code Jam 2013 - Qualification Round - Tic-Tac-Toe-Tomek
# http://code.google.com/codejam/contest/2270488/dashboard#s=p0
# © 2013 Aluísio Augusto Silva Gonçalves
# This Source Code Form is subject to the terms of the Mozilla Public License,
# version 2.0.  If a copy of the MPL was not distributed with this file, You
# can obtain one at http://mozilla.org/MPL/2.0/.


# Problem description {{{1
##########################

"""
   Tic-Tac-Toe-Tomek

"""


# Imports {{{1
##############

from __future__ import unicode_literals

import CodeJam


# Entry point {{{1
##################

@CodeJam.ProblemSolver(__name__, lines=5)
def solve (input):
    board = ''.join(input)
    # Build the possible solutions
    checks = (
        (board[0],  board[1],  board[2],  board[3]),
        (board[4],  board[5],  board[6],  board[7]),
        (board[8],  board[9],  board[10], board[11]),
        (board[12], board[13], board[14], board[15]),
        (board[0],  board[4],  board[8],  board[12]),
        (board[1],  board[5],  board[9],  board[13]),
        (board[2],  board[6],  board[10], board[14]),
        (board[3],  board[7],  board[11], board[15]),
        (board[0],  board[5],  board[10], board[15]),
        (board[3],  board[6],  board[9],  board[12]),
    )
    for c in checks:
        for pl in ('X', 'O'):
            nr = c.count(pl)
            if (nr == 4) or (nr == 3 and c.count('T') == 1):
                return '%s won' % pl
    # No player won; so draw or incomplete
    if board.count('.') == 0:
        return 'Draw'
    return 'Game has not completed'
