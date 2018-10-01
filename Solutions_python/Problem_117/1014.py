from __future__ import absolute_import, division, print_function

import sys

def solveCase():
    rows, cols = (int(x) for x in sys.stdin.readline().strip().split(' '))
    lawn = [[int(x) for x in sys.stdin.readline().strip().split(' ')] for _ in range(rows)]
    #print(rows, cols)
    #for row in lawn:
    #    print(' '.join(str(col) for col in row), ' ', max(row))
    
    # Trivial case
    if rows == 1 or cols == 1:
        return "YES"
    
    rowmax = [max(row) for row in lawn]
    for j in range(cols):
        colmax = max(lawn[i][j] for i in range(rows))
        for i in range(rows):
            x = lawn[i][j]
            if x == colmax: continue
            if x < rowmax[i]: return "NO"
    return "YES"

if __name__ == "__main__":
    for i in range(1, 1+int(sys.stdin.readline().strip())):
        print('Case #', i, ': ', solveCase(), sep='', end='\n')
