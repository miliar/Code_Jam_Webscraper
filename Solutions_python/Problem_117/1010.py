
def expand(x,y,number,matrixStarter,matrixGoal,matrixSize,gone):
    #line expand
    for j in range((int)(matrixSize[1])):
        if matrixStarter[x][j] in gone and matrixStarter[x][j] == int(matrixGoal[x][j]):
            break
        if j == (int)(matrixSize[1])-1:
            for jj in range((int)(matrixSize[1])):
                matrixStarter[x][jj] = number
    #column expand
    for j in range((int)(matrixSize[0])):
        if matrixStarter[j][y] in gone and matrixStarter[j][y] == int(matrixGoal[j][y]):
            break
        if j == (int)(matrixSize[0])-1:
            for jj in range((int)(matrixSize[0])):
                matrixStarter[jj][y] = number

def compareMatrix(a,b):
    for x in range(len(a)):
        for y in range(len(a[0])):
            if a[x][y] != int(b[x][y]):
                return 'NO'
    return 'YES'

if __name__ == "__main__":
    numberOfTests = (int)(input())
    for _ in range(numberOfTests):
        matrixSize = input().split(' ')
        matrixGoal = []
        
        for x in range((int)(matrixSize[0])):
            matrixGoal.append(input().split(' '))
        
        matrixStater = [[100 for _ in range((int)(matrixSize[1]))] for _ in range((int)(matrixSize[0]))]
        
        listOfNumbers = []
        
        for a in matrixGoal:
            for b in a:
                if int(b) not in listOfNumbers:
                    listOfNumbers.append(int(b))
        listOfNumbers.sort(reverse=True)
        
        gone = []
        for number in listOfNumbers:
            for x in range((int)(matrixSize[0])):
                for y in range((int)(matrixSize[1])):
                    if int(matrixGoal[x][y]) == number:
                        expand(x,y,number,matrixStater,matrixGoal,matrixSize,gone)
            gone.append(number)
                  
        print('Case #'+str(_+1)+': ' + compareMatrix(matrixStater,matrixGoal))
                    
