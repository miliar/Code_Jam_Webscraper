# by Enrique Gonzalez (Enriikke)
# enjoy!

# Setup the files here.
in_file = '../../../Downloads/A-large.in'
out_file = 'solution.out'
try:
    in_file = open(in_file, 'r')
    out_file = open(out_file, 'w')
except IOError as e:
    print e.errno
    print e.strerror


# Quick util function to print out a single case solution.
def print_solution(case_number, solution, file=out_file):
    try:
        file.write('Case #{0!s}: {1}\n'.format(case_number, solution))
    except Exception as e:
        print type(e)
        print e.args


# This is just a place holder and it makes it easier to read the code.
def parse_data(file=in_file):
    board_map = {}
    is_full = True
    for i in range(1, 5):
        row = in_file.readline().strip()
        if row.find('.') > -1: is_full = False
        board_map['row' + str(i)] = row
    
    
    key_list = board_map.keys()
    key_list.sort() 
        
    cols = []
    for i in range(4):
        col = []
        for key in key_list:
            col.append(board_map[key][i])
            
        cols.append(''.join(col))
    
    diags = []
    diag = []
    d = 0
    for key in key_list:
        diag.append(board_map[key][d])
        d = d + 1
    diags.append(''.join(diag))
    
    diag = []
    d = 3
    for key in key_list:
        diag.append(board_map[key][d])
        d = d - 1
    diags.append(''.join(diag))
    
    for i in range(1, 5):
        board_map['col' + str(i)] = cols[i - 1]
    
    for i in range(1, 3):
        board_map['diag' + str(i)] = diags[i - 1]
        
    board_map['is_full'] = is_full
    in_file.readline()
        
    return board_map
    


def solve_it():
    # Number of test cases
    N = int(in_file.readline())
    
    # Iterate through every test case
    for n in range(1, N + 1):
        # Get my case data ready
        board = parse_data()
        
        # Magic goes here
        solution = ''
        winner = False
        
        if board['row1'].replace('T', 'X') == 'XXXX': winner = 'X won'
        elif board['row1'].replace('T', 'O') == 'OOOO': winner = 'O won'
        
        elif board['row2'].replace('T', 'X') == 'XXXX': winner = 'X won'
        elif board['row2'].replace('T', 'O') == 'OOOO': winner = 'O won'
        
        elif board['row3'].replace('T', 'X') == 'XXXX': winner = 'X won'
        elif board['row3'].replace('T', 'O') == 'OOOO': winner = 'O won'
        
        elif board['row4'].replace('T', 'X') == 'XXXX': winner = 'X won'
        elif board['row4'].replace('T', 'O') == 'OOOO': winner = 'O won'
        
        elif board['col1'].replace('T', 'X') == 'XXXX': winner = 'X won'
        elif board['col1'].replace('T', 'O') == 'OOOO': winner = 'O won'
        
        elif board['col2'].replace('T', 'X') == 'XXXX': winner = 'X won'
        elif board['col2'].replace('T', 'O') == 'OOOO': winner = 'O won'
        
        elif board['col3'].replace('T', 'X') == 'XXXX': winner = 'X won'
        elif board['col3'].replace('T', 'O') == 'OOOO': winner = 'O won'
        
        elif board['col4'].replace('T', 'X') == 'XXXX': winner = 'X won'
        elif board['col4'].replace('T', 'O') == 'OOOO': winner = 'O won'
        
        elif board['diag1'].replace('T', 'X') == 'XXXX': winner = 'X won'
        elif board['diag1'].replace('T', 'O') == 'OOOO': winner = 'O won'
        
        elif board['diag2'].replace('T', 'X') == 'XXXX': winner = 'X won'
        elif board['diag2'].replace('T', 'O') == 'OOOO': winner = 'O won'
        
        elif board['is_full']: winner = 'Draw'
        
        
        if winner: solution = winner
        else: solution = 'Game has not completed'
        
        # Print solution
        print_solution(n, solution)
    
    
    # Close both files
    in_file.close()
    out_file.close()


solve_it()
