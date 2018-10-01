import os
from numpy import array

def solve(board):
    
    o = board == 'O'
    x = board == 'X'
    row, col = (board == 'T').nonzero()
    if len(row):
        row = row[0]
        col = col[0]
        o[row, col] = x[row, col] = True
 
    for i in range(4):
        if o[i].all() or o[:,i].all():
            return 'O won'
        if x[i].all() or x[:,i].all():
            return 'X won'
     
    if o.diagonal().all() or all([o[i,-i-1] for i in range(4)]):
        return 'O won'
    if x.diagonal().all() or all([x[i,-i-1] for i in range(4)]):
        return 'X won'
    
    if (board == '.').sum():
        return 'Game has not completed'
    return 'Draw'
    


def main(filename):
    
    with open(filename) as inp: 
        n_cases = inp.readline().strip()
        n_cases = int(n_cases)
        
        with open(os.path.join(os.path.split(filename)[0], '.out'), 'w') as out:
        
            for i in range(n_cases):
                board = array([list(inp.readline().strip()) for j in range(4)])
                out.write('Case #{}: {}\n'.format(i+1, solve(board)))
                inp.readline()
            


if __name__ == '__main__':
    
    main('A-large.in')
