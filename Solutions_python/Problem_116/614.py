import sys


def case(board):
    seen = 0
    #columns
    for i in range(4):
        c = check(board[i])
        if c > 0:
            return
        seen +=c   
    #rows
    for j in range(4):
        c = check(board[0][j]+board[1][j]+board[2][j]+board[3][j])
        if c > 0:
            return
        seen +=c   

    #diag
    c = check(board[0][0]+board[1][1]+board[2][2]+board[3][3])
    if c > 0:
        return
    seen +=c   
    c = check(board[0][3]+board[1][2]+board[2][1]+board[3][0])
    if c > 0:
        return
    seen +=c   
    if c==0:
        print("Draw")
    else:    
        print("Game has not completed")
    return

def check(line):
    if '.' in line:
        return -1
    if ('X' in line) and ('O' in line):
        return 0
    if ('X' in line):
        print("X won")
        return 1
    print("O won")
    return 2

def work(fin):
    n = int(fin.readline())
    for i in range(n):
        print("Case #",i+1,": ",end="",sep="")
        board = []
        for j in range(4):
            board.append(fin.readline().strip())
        case(board)
        fin.readline()

if __name__ == "__main__":
    INPUT = sys.argv[1]

    fin = open(INPUT,'r')
    work(fin)
