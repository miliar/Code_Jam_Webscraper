'''
Template

@author: Mohammad
'''

def main():  
    inn = open("A-large.in", "r")
    out = open("out.txt", "w")
    T = int(inn.readline())
   
    
    for t in range(T):
        board = []
        lines = []
        x = False
        o = False
        over = True
        for i in range(4):
            board.append(inn.readline().strip('\n'))
            lines.append(board[i])
        inn.readline()
                
        d1 = ""
        d2 = ""
        for j in range(4):
            col = ""
            for i in range(4):
                col += board[i][j]
                if i == j:
                    d1 += board[i][j]
                if i == 3 - j:
                    d2 += board[i][j]
            lines.append(col)
        lines.append(d1)
        lines.append(d2)
        
        for line in lines:
            if line == 'XXXX':
                x = True
            if line == 'OOOO':
                o = True
            if '.' in line:
                over = False
            elif 'T' in line:
                if not('O' in line):
                    x = True
                if not('X' in line):
                    o = True
        out.write('Case #' + str(t+1) + ': ')
        if x == True:
            out.write('X won')
        elif o == True:
            out.write('O won')
        elif over == True:
            out.write('Draw')
        else:
            out.write('Game has not completed')
        out.write('\n')
    inn.close()
    out.close()
main()
