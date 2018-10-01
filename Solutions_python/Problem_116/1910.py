
file = open("A-large.in", 'r')

first = 1
boards = 0
count = 0

four=0
string_board = ""
full_board = 1

def handle_T(a, b, c, d):
    if a=='T':
        if (b==c) and (c==d):
            if b!='.':
                return b
            else:
                return '.'
        else:
            return '.'
    elif b=='T':
        if (a==c) and (c==d):
            if a!='.':
                return a
            else:
                return '.'
        else:
            return '.'
    elif c=='T':
        if (b==a) and (a==d):
            if b!='.':
                return b
            else:
                return '.'
        else:
            return '.'
    elif d=='T':
        if (b==c) and (c==a):
            if b!='.':
                return b
            else:
                return '.'
        else:
            return '.'
    else:
        if (a==b) and (b==c) and (c==d):
            return a
        else:
            return '.'

def check_for_win():
    #print string_board
    win = ""
    win += handle_T(string_board[0],string_board[1],string_board[2],string_board[3])
    win += handle_T(string_board[4],string_board[5],string_board[6],string_board[7])
    win += handle_T(string_board[8],string_board[9],string_board[10],string_board[11])
    win += handle_T(string_board[12],string_board[13],string_board[14],string_board[15])
    win += handle_T(string_board[0],string_board[4],string_board[8],string_board[12])
    win += handle_T(string_board[1],string_board[5],string_board[9],string_board[13])
    win += handle_T(string_board[2],string_board[6],string_board[10],string_board[14])
    win += handle_T(string_board[3],string_board[7],string_board[11],string_board[15])
    win += handle_T(string_board[0],string_board[5],string_board[10],string_board[15])
    win += handle_T(string_board[3],string_board[6],string_board[9],string_board[12])
    #print win
    for char in win:
        if char != '.':
            return char
    return '.'

def print_result():
    full_board = 1
    for char in string_board:
        if char == '.':
            full_board = 0
    #print winner
    #print full_board
    win_string = "Case #"+repr(count)+": "
    if (winner == 'X') or (winner == 'O'):
        win_string += winner + " won"
    elif (winner == '.'):
        if full_board == 1:
            win_string += "Draw"
        else:
            win_string += "Game has not completed"
    print win_string

for line in file:
    if (first == 1):
        boards = int(line)
        first = 0
    else:
        four += 1
        #print four
        if (four <= 4):
            string_board += line[0:4]
        elif (four == 5):
            four = 0
            winner = check_for_win()
            count += 1
            print_result()
            string_board = ""
    #print line

count += 1
winner = check_for_win()
print_result()

file.close()
