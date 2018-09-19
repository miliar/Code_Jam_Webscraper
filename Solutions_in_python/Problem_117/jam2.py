'''
Created on 13. apr. 2013

@author: null
'''
def checkArray(value,array):
    for x in array:
        if not (x <= value):
            return False
    return True

def checkGame(game,n,m):
    for i in xrange(n):
        for j in xrange(m):
            #check row
            if not (checkArray(game[i][j],game[i]) or checkArray(game[i][j],[game[k][j] for k in xrange(n)])):
                return 0
    return 1

if __name__ == '__main__':
    f = open("ttt1.txt")
    t = int(f.readline().strip())
    
    for i in xrange(t):
        temp1 = f.readline().strip()
        temp1 = temp1.split(" ")
        n = int(temp1[0])
        m = int(temp1[1])
        
        game = []
        for j in xrange(n):
            temp2 = f.readline().strip()
            temp2 = temp2.split(" ")
            temp2 = [int(x) for x in temp2]
            game.append(temp2)
            
        result = checkGame(game,n,m)
        
        resultString = "Case #"+ str(i+1) +": " 
        if result == 0:
            resultString += "NO"
        elif result == 1: 
            resultString += "YES"
        print resultString
    
    f.close()