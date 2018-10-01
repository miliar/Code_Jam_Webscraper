import math
f = open('DInput.txt')
lines = f.readlines()
f.close()


output = open('DOutput.txt','w')

for i in range(int(lines[0])):
    X = int(lines[i+1].split()[0])
    R = int(lines[i+1].split()[1])
    C = int(lines[i+1].split()[2])
    print X,
    print R,
    print C,
    winner = "Richard"
    if(X >= 7):
        winner = "Richard"
    elif(X == 1):
        winner = "GABRIEL"
    elif(X == 2):
        if(R*C%2):
            winner = "Richard"
        else:
            winner = "GABRIEL"
    elif(X==3):
        if((R%3==0 and C>1) or (C%3==0 and R>1)):
            winner = "GABRIEL" #pick L or straight
        else:
            winner = "Richard"
    elif(X==4):
        if(R<4 and C<4):
            winner = "Richard" #just pick the 1x4
        elif(R==1 or C==1):
            winner = "Richard" #just pick the 2x2
        elif(R%2 and C%2):
            winner = "RICHARD" #does not work
        elif((R==4 and C ==2) or (R==2 and C ==4)):
            winner = "RICHARD" #pick the z shape
        else:
            winner = "GABRIEL"
    elif(X==5):
        if(R<5 and C<5):
            winner = "RICHARD" #just pick the 1x5
        elif(R==1 or C==1):
            winner = "RICHARD" #just pick the 2x3
        elif(R%2 and C%2):
            winner = "RICHARD" #does not work
        else:
            winner = "GABRIEL"
    elif(X==6):
        if(R<6 and C>6):
            winner = "RICHARD" #just pick the 1x6
        elif(R==1 or C==1):
            winner = "RICHARD" #just pick the 2x3
        elif(R%2 and C%2):
            winner = "RICHARD" #does not work
        else:
            winner = "GABRIEL"
        
    #In all cases if R*C%X richard wins
    if(R*C%X):
        winner = "RICHARD"
        
    print winner
    output.write("Case #")
    output.write(str(i+1))
    output.write(": ")
    output.write(winner)
    output.write("\n")
        
output.close()         