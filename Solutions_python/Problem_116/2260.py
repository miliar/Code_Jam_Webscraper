#!/usr/bin/env python
# tictactoe.py
#==============================================================================
#
# 0   1  2  3 
# 4   5  6  7 
# 8   9 10 11
# 12 13 14 15
#
#==============================================================================

def read(fname):
    """
    Read input file.
    """
    debug = 0
    if debug: print "read"

    f = open(fname, "r")
    t = int(f.readline())
    if debug: print "t ", t

    games = {}
    for igame in range(1, t+1):
        if debug: print "igame ", igame
        data = ""
        for irow in range(0, 4):
            l = f.readline().strip()
            if debug: print "l ", l
            data += l
        if debug: print "data ", data
        games[igame] = data
        f.readline()

    f.close()

    return t, games

#==============================================================================

def win_row(row):
    """
    Determine if a row wins.

    Returns 0 if no winner, 1 if X wins or 2 if O wins.
    """
    status = 0
    if "." in row: return status

    if "T" in row:
        if   row.count("X")==3: return 1
        elif row.count("O")==3: return 2
    
    if   row.count("X")==4: return 1
    elif row.count("O")==4: return 2

    return 0

#==============================================================================

def play(t, games):
    """
    Play the tic tac toe game.
    """
    debug = 1
    if debug: print "play"

    if debug: print "t ", t

    # Dimensions
    nrows = 4
    ncols = 4    

    igames = games.keys()
    igames.sort()
    if debug: print "igames ", igames

    fname = "output.txt"
    f = open(fname, "w")

    for igame in igames:
        if debug: print "igame ", igame

        # Status. 0: not completed, 1: X win, 2: O win, 3: draw
        status = 0

        data = games[igame]
        if debug: print "data ", data

        # Check rows
        for irow in range(0, nrows):
            row = data[irow*ncols:(irow+1)*ncols]
            status = win_row(row)
            if status: break

        # Check columns
        if not status:
            for icol in range(0, ncols):
                col = data[icol] + data[(1*ncols)+icol] + data[(2*ncols)+icol] + data[(3*ncols)+icol]
                status = win_row(col)
                if status: break

        # Check diagonal 1 
        if not status:
            diag1 = data[0] + data[5] + data[10] + data[15]
            status = win_row(diag1)

        # Check diagonal 2 
        if not status:
            diag2 = data[3] + data[6] + data[9] + data[12]
            status = win_row(diag2)

        # Check draw
        if not status:
            if not '.' in data:
                status = 3
        
        # Write status
        f.write("Case #%i: "%igame)
        if status==0  : f.write("Game has not completed")
        elif status==1: f.write("X won")
        elif status==2: f.write("O won")
        elif status==3: f.write("Draw")
        f.write("\n")

    f.close()
        
#==============================================================================

if __name__ == "__main__":

    import os, sys
    args = sys.argv
    if not len(args)==2:
        print "Usage: %s input_filename"%args[0]
        sys.exit(1)
    fname = args[1]
    if not os.path.isfile(fname):
        print "File '%s' do not exist"%fname
        sys.exit(1)
    t, games = read(fname)
    play(t, games)

#==============================================================================
