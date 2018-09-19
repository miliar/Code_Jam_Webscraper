#INPUT PARSING
f = open('A-large.in','r')
input_file = [x.strip() for x in f.readlines()]
f.close()

n_cases = int(input_file.pop(0))
input_cases = []

while len(input_file)>0:
    board = [ [x for x in y] for y in input_file[:4]]
    input_file = input_file[5:]
    input_cases.append(board)
    


# SUBFUNCTIONS

def check_for_incomplete(query_board):
    for x in query_board:
        for y in x:
            if y == '.':
                return True
    return False

def check_for_victory(query_line):
    if query_line[0] == 'T':
        victor = query_line[1]
    else:
        victor = query_line[0]
    for x in query_line:
        if (x == '.') or ((x != victor) and (x != 'T')):
            return None
    return victor


#MAIN SOLUTION FUNCTION

def solve_problem(board):
    #First, check to see if there is a victor
    victor = None
    
    #check rows
    for x in board:
        test_result = check_for_victory(x)
        if test_result:
            victor = test_result
        
    #check columns
    columns = [ [x[i] for x in board] for i in range(len(board))]
    for x in columns:
        test_result = check_for_victory(x)
        if test_result:
            victor = test_result
    #check diagonals
    diagonals = [ [ board[i][i] for i in range(len(board))], [ board[i][3-i] for i in range(len(board))] ]
    for x in diagonals:
        test_result = check_for_victory(x)
        if test_result:
            victor = test_result
    
    if victor:
        return victor + ' won'
    elif check_for_incomplete(board):
        return 'Game has not completed'
    else:
        return 'Draw'


#OUTPUT SOLUTIONS

f = open('A_large_solution.txt','w')
for i,x in enumerate(input_cases):
    f.write('Case #' + str(i+1) + ': ' + solve_problem(x) + '\n')
f.close()