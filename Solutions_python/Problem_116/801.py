#!/usr/bin/env/python
# Google Code Jam Qualification Round
# Author: Nick Mooney

from itertools import chain
from sys import argv

def check_game(positions):
    """Takes a list of four lists of four characters, outputs who won the game,
    or 'I' in case of incomplete, or 'D' in case of draw."""
    rows_to_check = []
    
    # First let's handle the diagonals
    rows_to_check.append([positions[x][x] for x in range(4)])
    rows_to_check.append([positions[3-x][x] for x in range(4)])
    
    # Columns and row
    for i in range(4):
        rows_to_check.append([positions[x][i] for x in range(4)]) # Columns
        rows_to_check.append(positions[i]) # Rows
    
    for row in rows_to_check:
        result = check_row(row)
        if result is not None:
            return result
    
    # By this point the game has not been won.
    
    # Still more moves to make
    if '.' in list(chain.from_iterable(positions)):
        return 'I'
    else: # Or not
        return 'D'

def check_row(row):
    """Takes a row (or column, or diagonal) and outputs who won,
    or outputs None in case of no win."""
    row = sorted(set(row))
    if '.' in row:
        return None
    elif 'T' in row:
        row.remove('T')
    
    if len(row) == 1:
        return row[0]
    else:
        return None

if __name__ == "__main__":
    try:
        tictacsomething_filename = argv[1]
        outfile_filename = argv[2]
    except:
        print("Usage: codejam_qual.py <infile> <outfile>")
    
    ttt_file = open(tictacsomething_filename,'r').read().splitlines()
    out_file = open(outfile_filename, 'w')
    
    number_games = int(ttt_file[0])
    del(ttt_file[0])

    for game in range(number_games):
        positions = list()
        for i in range(4):
            positions.append(list(ttt_file[0]))
            del(ttt_file[0])

        result = check_game(positions)
        if result is 'X' or result is 'O':
            out_file.write("Case #%d: %s won\n" % (game + 1, result))
        elif result is 'D':
            out_file.write("Case #%d: Draw\n" % (game + 1))
        else:
            out_file.write("Case #%d: Game has not completed\n" % (game + 1))
        
        del(ttt_file[0]) # Get rid of the newline
    
