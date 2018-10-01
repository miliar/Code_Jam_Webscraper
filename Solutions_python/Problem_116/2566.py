"""
Tic-Tac-Toe-Tomek
"""
import sys
from pandas import *

def solve(testcase):
    x_wins = False
    o_wins = False
    full_board = True
    df = DataFrame(testcase)
    
    # rows
    for row in range(4):
        if all(True if i == True or i == "T" else False for i in df.ix[row].values):
            o_wins = True
        elif all(True if i == False or i == "T" else False for i in df.ix[row].values):
            x_wins = True
        if any(i == None for i in df.ix[row].values):
            full_board = False
        
    # cols
    for col in range(4):
        if all(True if i == True or i == "T" else False for i in df.ix[:, col:col].values):
            o_wins = True
        elif all(True if i == False or i == "T" else False for i in df.ix[:, col:col].values):
            x_wins = True
    # diag tl -> lr
    rows = range(4)
    cols = range(4)
    if not o_wins:
        if all(True if df.ix[row][col] == True or df.ix[row][col] == "T" else False for row, col in zip(rows, cols)):
            o_wins = True
    if not x_wins:
        if all(True if df.ix[row][col] == False or df.ix[row][col] == "T" else False for row, col in zip(rows, cols)):
            x_wins = True
    
    # diag tr -> ll
    cols.sort(reverse=True)
    if not o_wins:
        if all(True if df.ix[row][col] == True or df.ix[row][col] == "T" else False for row, col in zip(rows, cols)):
            o_wins = True
    if not x_wins:
        if all(True if df.ix[row][col] == False or df.ix[row][col] == "T" else False for row, col in zip(rows, cols)):
            x_wins = True        
        
    result = "Game has not completed"
    if x_wins and o_wins:
        result = "Draw"
    elif x_wins:
        result = "X won"
    elif o_wins:
        result = "O won"
    elif not x_wins and not o_wins and full_board:
        result = "Draw"
    return result
        

if __name__ == "__main__":
    in_f = open(sys.argv[1], "r")
    n_testcases = int(in_f.readline())
    nrows = 4
    O = True
    X = False
    for i in range(1, n_testcases + 1):
        testcase = []
        for row in range(nrows):
            trow = []
            line = in_f.readline().strip()
            assert len(line) == 4
            for c in line:
                if c == "O":
                    trow.append(True)
                elif c == "X":
                    trow.append(False)
                elif c == "T":
                    trow.append("T")
                else:
                    trow.append(None)
            testcase.append(trow)
        assert len(testcase) == 4
        r = solve(testcase)
        print "Case #{}: {}".format(i, r)
        # skip blank line
        _ = in_f.readline()
        
    
    