#!/usr/bin/env python
NUM_OF_ELEMENTS_PER_PROBLEM = 5

# possible solutions
X_WON = 'X won'
O_WON = 'O won'
ONGOING = 'Game has not completed'
DRAW = 'Draw'

def winner(matrix, player):
    points = { 'rows' : [0,0,0,0],
                'cols' : [0,0,0,0]
    }
    # check the cols and rows
    for row_no,row in enumerate(matrix):
        for cell_no, cell in enumerate(row):
            if cell == player or cell == 'T':
                points['rows'][row_no] += 1
                points['cols'][cell_no] += 1
                if points['rows'][row_no] == 4 or points['cols'][cell_no] == 4:
                    return True
    
    #if not yet finished, check horizontal
    row_no = 0
    col_no = 0
    sum_diag = 0
    while row_no < 4:
        if matrix[row_no][col_no] == player or matrix[row_no][col_no] == 'T':
            sum_diag += 1
            if sum_diag == 4:
                return True
        row_no += 1
        col_no = row_no
        
    row_no = 0
    col_no = 3
    sum_diag = 0
    while row_no < 4:
        if matrix[row_no][col_no] == player or matrix[row_no][col_no] == 'T':
            sum_diag += 1
            if sum_diag == 4:
                return True
        row_no += 1
        col_no -= 1


def solve(probleminput):
    """
    in: expects a list of inputs for the current testcase. see NUM_OF_ELEMENTS_PER_PROBLEM for the list size
    out: should return the solution for this testcase
    """
    matrix = [
      probleminput[0][:4],
      probleminput[1][:4],
      probleminput[2][:4],
      probleminput[3][:4]
    ]
    
    unused_cells = True if '.' in matrix.__str__() else False

    x_won = winner(matrix, 'X')
    o_won = winner(matrix, 'O')
    
    if(x_won): 
        return X_WON
    elif (o_won):
        return O_WON
    else:
        return ONGOING if unused_cells else DRAW

###### program skeleton #######
import sys
problem = [l.replace('\n', '') for l in sys.stdin.readlines()]
for testcase in xrange(1, int(problem[0]) + 1):
    begin = 1 + (testcase - 1) * NUM_OF_ELEMENTS_PER_PROBLEM
    result = solve(problem[begin:begin + NUM_OF_ELEMENTS_PER_PROBLEM])
    print "Case #%i: %s" % (testcase, result)
