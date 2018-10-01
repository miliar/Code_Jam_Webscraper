import sys

def checkResult(line):
    
    temp = line[0]
    if('.' in line):
        return False
    
    for i in line[1:]:
        if(i != temp and i != 'T' and temp != 'T'):
            return False
        temp = i
    return True
        

f = open(sys.argv[1],"r")
output = open("tictactoetomek.txt","w")
num = int(f.readline())
test_cases = f.read()
test_cases = test_cases.split("\n")


final = []

counter = 0
for i in test_cases:
    if(i):
        if counter == 0:
            final.append([])
        final[-1].append(i)
        counter = (counter + 1) % 4

case = 0
for z in final:
    case += 1
    dot = False
    winner = None
    diag = [[],[]]
    
    for i in range(4):

        hor = []
        ver = []
        for j in range(4):
            if dot == False and z[i][j] == '.':
                dot = True
            hor.append(z[i][j])
            ver.append(z[j][i])
            if i == j:
                diag[0].append(z[i][j])
            if i+j == 3:
                diag[1].append(z[i][j])
        if(checkResult(hor)):
            for data in hor:
                if data != 'T':
                    winner = data
                    break
            break
        elif(checkResult(ver)):
            for data in ver:
                if data != 'T':
                    winner = data
                    break
            break
    if(winner == None):
        if(checkResult(diag[0])):
            for data in diag[0]:
                if data != 'T':
                    winner = data
                    break 
                       
    if(winner == None):
        if(checkResult(diag[1])):
            for data in diag[1]:
                if data != 'T':
                    winner = data
                    break
    if(winner == None and dot == True):
        winner = "Game has not completed"
    elif(winner == None and dot == False):
        winner = "Draw"    
    else:
        winner = winner + " won"
    output.write("Case #"+str(case)+": "+winner+"\n")