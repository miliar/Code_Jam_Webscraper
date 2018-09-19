
import sys

def check_diags(board, l, i, player):
    ret = False
    rows = len(board)
    cols = len(board[0])

    if l < rows and i < cols:
        if board[l][i] == player:
            ret = True
    return ret

def check_win(board, k, player):
    for l in board:
        if k*player in l:
            return True
    for i in range(len(board[0])):
        l = ''.join([j[i] for j in board])
        if k*player in l:
            return True

    ret = False
    for l in range(len(board)):
        for i in range(len(board[0])):
            if board[l][i] == player:
                ret = True
                for j in range(1, k):
                    if not check_diags(board, l+j, i+j, player):
                        ret = False
                        break
                if ret: return ret
                else: ret = True
                for j in range(1, k):
                    if not check_diags(board, l+j, i-j, player):
                        ret = False
                        break
                if ret: return ret
    return ret

def rotate(line):
    ret = ''
    for i in line:
        if i == '.':
            ret = i + ret
        else:
            ret += i
    return ret

if __name__ == '__main__':
    stdin = sys.stdin
    num_cases = stdin.readline()

    for i in range(int(num_cases)):
        line = stdin.readline()
        N, K = map(int, line.split())

        board = []
        for l in range(N):
            line = stdin.readline()
            board.append(rotate(line.strip()))

        R = check_win(board, K, 'R')
        B = check_win(board, K, 'B')

        #for l in board:
            #print l

        res = 'Neither'
        if R and B:
            res = 'Both'
        elif R:
            res = 'Red'
        elif B:
            res = 'Blue'

        print "Case #%d: %s" % (i+1, res)
