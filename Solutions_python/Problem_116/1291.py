"""
2013 - qualification Problem A
Tic-Tac-toe-tomek
"""

"""
We are checking case on 
1. X won
2. O won
3. Draw
4. Not complete
"""
dotFlag = False

def CaseCheck(row):
    if not '.' in row:
        if 'X' in row and not 'O' in row:
            return 'X won'
        if 'O' in row and not 'X' in row:
            return 'O won'
        return False
    global dotFlag 
    dotFlag = True
    return False

def HorizontalCheck(board):
    for row in board:
        r = CaseCheck(row)
        if r:
            return r
    return False


def VerticalCheck(board):
    for i in range(4):
        col = [row[i] for row in board]
        r = CaseCheck(col)
        if r:
            return r
    return False

def DiagonalCheck(board):
    dia1 = [board[0][0], board[1][1], board[2][2], board[3][3]]
    r = CaseCheck(dia1)
    if r:
        return r
    dia2 = [board[0][3], board[1][2], board[2][1], board[3][0]]
    r = CaseCheck(dia2)
    if r:
        return r
    return False

def CompleteCheck(board):
    if dotFlag:
        return "Game has not completed"
    else:
        return "Draw"

def main():
    f = open('A-large.in', 'r')
    r = open('A-large.in-result', 'w')

    while True:
        line = f.readline()
        if not line:
            break
        totalCaseNum = int(line)
        for i in range(totalCaseNum):
            global dotFlag 
            dotFlag = False
            board = []
            for j in range(4):
                temp = f.readline()
                row = [x for x in temp]
                board.append(row)
            f.readline() #emptyline
            # ready to check case
            result = HorizontalCheck(board) or VerticalCheck(board) or DiagonalCheck(board) or CompleteCheck(board)
            result_line = 'Case #' + str(i + 1) + ': ' + result
            r.write(result_line + '\n')
            print result_line


    f.close()
    r.close()



if __name__ == '__main__':
    main()