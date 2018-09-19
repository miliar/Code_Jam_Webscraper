import sys
from copy import copy
from collections import deque
from time import sleep

qty_test_cases = int(sys.stdin.readline())

class ImpossibleException(Exception):
    pass

def changeDataColor(rows_data, row, col, new_val):
    if rows_data[row][col] == "#":
        rows_data[row][col] = new_val
    else:
        raise ValueError()

def changeColor(rows_data, row):
    try:
        start_col = rows_data[row].index("#")
    except ValueError:
        return False
    
    try:
        rows_data[row][start_col] = "/";
        changeDataColor(rows_data, row, start_col+1, "\\")
        changeDataColor(rows_data, row+1, start_col, "\\")
        changeDataColor(rows_data, row+1, start_col+1, "/")
    
        return True
    except Exception:
       raise ImpossibleException("Impossible")


for i in range(0,qty_test_cases):
    print "Case #%d:" % (i+1)
    
    qty_rows, qty_cols = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    rows = list()
    
    for j in range(0, qty_rows):
        rows.append( list(sys.stdin.readline().strip())[0:qty_cols] )
    
    # if i == 0:
    #     continue
    
    partial_out = ""
    
    try:
        for row_index in range(0, qty_rows):
            while changeColor(rows, row_index):
                pass
            partial_out += "".join(rows[row_index]) + "\n"
        
        print partial_out,
    except ImpossibleException:
        print("Impossible")