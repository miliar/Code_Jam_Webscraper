'''
Created on 2013-4-13

@author: t
'''


def test(board):
    for i in range(4):
        result_line = check(board[i])
#        if result_line == 0:
#            return 'Game has not completed'
#        if result_line == 1:
#            continue
        if result_line == 2:
            return 'X won'
        if result_line == 3:
            return 'O won'
    
    for i in range(4):
        vertical = []
        vertical.append(board[0][i])
        vertical.append(board[1][i])
        vertical.append(board[2][i])
        vertical.append(board[3][i])
        result_line = check(vertical)
#        if result_line == 0:
#            return 'Game has not completed'
#        if result_line == 1:
#            continue
        if result_line == 2:
            return 'X won'
        if result_line == 3:
            return 'O won'
    
    diagonal=[]
    diagonal.append(board[0][0])
    diagonal.append(board[1][1])
    diagonal.append(board[2][2])
    diagonal.append(board[3][3])
    result_line = check(diagonal)
#    if result_line == 0:
#        return 'Game has not completed'
    if result_line == 2:
        return 'X won'
    if result_line == 3:
        return 'O won' 
    
    diagonal=[]
    diagonal.append(board[0][3])
    diagonal.append(board[1][2])
    diagonal.append(board[2][1])
    diagonal.append(board[3][0])
    result_line = check(diagonal)
#    if result_line == 0:
#        return 'Game has not completed'
    if result_line == 2:
        return 'X won'
    if result_line == 3:
        return 'O won'   
    
    
    for line in board:
        if '.' in line:
            return 'Game has not completed'
    
    return 'Draw'  
            
            
    
    
    
    
    
    
    
def check(line):
    if '.' in line:
        return 0 #not completed
    for i in range(1,4):
        if compare(line[i],line[i-1]):
            continue
        else:
            return 1 #no one win
    
    
    return getWinner(line[0],line[1]) 
    
        
    

def getWinner(a,b):
    if a!= 'T':
        return transform(a)
    else:
        return transform(b)
  
def transform(a):
    if a == 'X':
        return 2
    if a == 'O':
        return 3
    print "error"
    return 'error' 



def compare(a,b):
    if a == b:
        return True
    if (a == 'T') or (b == 'T'):
        return True
    return False        
        
    


if __name__ == "__main__":
    inputfile = open("A-small-attempt0.in",'r')
    
    outputfile = open('result','w')
    num_test = int(inputfile.readline())
    for i in range(num_test):
        board = []
        for k in range(4):
            board.append(inputfile.readline())
        outputfile.write('Case #'+str(i+1)+': '+test(board)+'\n')
        jump = inputfile.readline()
#    test(board)