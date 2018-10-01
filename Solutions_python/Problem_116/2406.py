#!/usr/bin/python

num=None
count = 0

boards = []
ii = jj = 0

# def resolve(board):
#     for line in range(4):
#         for row in board[line]:
def print_board(board):
    for ii in range(4):
        print board[ii*4:ii*4+4]
    print ""

def result(cell0,cell1,cell2,cell3):
    list = [cell0,cell1,cell2,cell3]
    if not "T" in list:
        if list.count("X") == 4:
            return "X won"
        elif list.count("O") == 4:
            return "O won"
        else:
            return None
    else:
        if list.count("X") == 3:
            return "X won"
        elif list.count("O") == 3:
            return "O won"
        else:
            return None

def judge(board):
    for ii in range(4):
        temp = result(board[4*ii],board[4*ii+1],board[4*ii+2],board[4*ii+3])
        if temp is not None:
            return temp
        temp = result(board[ii],board[ii+4],board[ii+8],board[ii+12])
        if temp is not None:
            return temp
    temp = result(board[0],board[5],board[10],board[15])
    if temp is not None:
        return temp
    temp = result(board[3],board[6],board[9],board[12])
    if temp is not None:
        return temp
    if "." in board:
        return "Game has not completed"
    else:
        return "Draw"

#for line in open("A-small-attempt3.in","r"):
for line in open("A-large.in","r"):
    if num is None:
        num = int(line)
        for ii in range(num):
            boards.append([])
        ii = 0
    else:
        line = line[:-1]
        if count < num:
            if len(boards[count]) < 16:
                for ii in range(4):
                    boards[count].append(line[ii])
            else:
                ii = 0
                count += 1
    
ii = 0            
for board in boards:
    ii += 1
#    print judge(board)
#    print_board(board)
    print "Case #%d: %s"%(ii,judge(board))
