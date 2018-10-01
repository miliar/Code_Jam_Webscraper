def x_won(board):
    for i in range(4):
        h_x = 0
        v_x = 0
        d_x = 0
        di_x = 0
        for j in range(4):
            if (board[i][j] == 'X' or board[i][j] == 'T'):
                h_x += 1
            if (board[j][i] == 'X' or board[j][i] == 'T'):
                v_x += 1
            if (board[j][j] == 'X' or board[j][j] == 'T'):
                d_x += 1
            if (board[j][3-j] == 'X' or board[j][3-j] == 'T'):
                di_x += 1
				
        if (h_x == 4 or v_x == 4 or d_x == 4 or di_x == 4):
            return True
			
    return False
	
def o_won(board):
    for i in range(4):
        h_x = 0
        v_x = 0
        d_x = 0
        di_x = 0
        for j in range(4):
            if (board[i][j] == 'O' or board[i][j] == 'T'):
                h_x += 1
            if (board[j][i] == 'O' or board[j][i] == 'T'):
                v_x += 1
            if (board[j][j] == 'O' or board[j][j] == 'T'):
                d_x += 1
            if (board[j][3-j] == 'O' or board[j][3-j] == 'T'):
                di_x += 1
				
        if (h_x == 4 or v_x == 4 or d_x == 4 or di_x == 4):
            return True
			
    return False
	
def draw(board):
    for i in range(4):
        for j in range(4):
            if (board[i][j] == '.'):
                return False
    return True
	
	
def solve(input_1, input_2, input_3, input_4):
    board = [input_1, input_2, input_3, input_4]
    if (x_won(board)):
        return("X won")
    if (o_won(board)):
        return("O won")
    if (draw(board)):
        return("Draw")
    return("Game has not completed")
	
def process_tests(command_to_run):
    in_file = open('in')
    out_file = open("out","w")
    number_of_tests = int(in_file.readline())
    for test_case in range(number_of_tests):
        test_string_1 = in_file.readline()[:-1]
        test_string_2 = in_file.readline()[:-1]
        test_string_3 = in_file.readline()[:-1]
        test_string_4 = in_file.readline()[:-1]
        test_answer = command_to_run(test_string_1,test_string_2,test_string_3,test_string_4)
        out_file.write("Case #" + str(test_case + 1) + ": " + str(test_answer) + "\n")
        blank_string = in_file.readline()[:-1]
    out_file.close()
    in_file.close()
	
	
process_tests(solve)
