__author__ = 'pard'


def _is_run(chars):
    set_chars = set(chars.flat)
    set_chars = list(set_chars)
    winning_char = ''
    if len(set_chars) == 1:
        winning_char = set_chars[0]
    elif len(set_chars) == 2 and 'T' in set_chars:
        if set_chars[0] == 'T':
            winning_char = set_chars[1]
        else:
            winning_char = set_chars[0]
    if winning_char != '.':
        return winning_char
    else:
        return ''


def _row_search(board):
    for row in board:
        winning_char = _is_run(row)
        if winning_char != '':
            return winning_char
    return ''


def _col_search(board):
    for col in board.T:
        winning_char = _is_run(col)
        if winning_char != '':
            return winning_char
    return ''


def _diag_search(board):
    diag = board.diagonal()

    winning_char = _is_run(diag)
    if winning_char != '':
        return winning_char


def _rev_diag_search(board):
    rev_diag = board[::-1].diagonal()

    winning_char = _is_run(rev_diag)
    if winning_char != '':
        return winning_char


def algorithm(board):
    import numpy as np
    winning_char = _row_search(board) or _col_search(board) or _diag_search(board) or _rev_diag_search(board)
    if winning_char:
        output = winning_char + ' won'
    else:
        if np.any(board == '.'):
            output = 'Game has not completed'
        else:
            output = 'Draw'
    return output

