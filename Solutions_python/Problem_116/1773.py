def status(game):
    finalStatus=4
    if isTicTacToeTomek("X",game)==True:
        finalStatus=1
    else:
        if isTicTacToeTomek("O",game)==True:
            finalStatus=2
        else:
            for i in game:
                if i==".":
                    finalStatus=3
                    break
    return finalStatus

def isTicTacToeTomek(sym,game):
    isTTTT=False
    for i in range(0,13,4):
        isTTTT=True
        for j in range(i,i+4):
            if game[j]!=sym and game[j]!="T":
                isTTTT=False
                break
        if isTTTT==True:
            break
    if isTTTT==False:
        for i in range(0,4):
            isTTTT=True
            for j in range(i,i+13,4):
                if game[j]!=sym and game[j]!="T":
                    isTTTT=False
                    break
            if isTTTT==True:
                break
    if isTTTT==False:
        for i in range(0,16,5):
            isTTTT=True
            if game[i]!=sym and game[i]!="T":
                isTTTT=False
                break
    if isTTTT==False:
        for i in range(3,13,3):
            isTTTT=True
            if game[i]!=sym and game[i]!="T":
                isTTTT=False
                break
    return isTTTT

def output(gameStatus,caseNumber):
    fout=open("output.txt","a")
    if gameStatus==1:
        fout.write("Case #"+str(caseNumber)+": X won\n")
    else:
        if gameStatus==2:
            fout.write("Case #"+str(caseNumber)+": O won\n")
        else:
            if gameStatus==3:
                fout.write("Case #"+str(caseNumber)+": Game has not completed\n")
            else:
                fout.write("Case #"+str(caseNumber)+": Draw\n")
    fout.close()

f=open("A-large.in","r")
f.readline()
isEOF=False
result=0
caseCounter=1
f.seek(2)
while isEOF==False:
    game=[]
    partido=""
    line=f.readline()
    for i in range(0,4):
        line=f.readline()
        if not line:
            isEOF=True
            break
        else:
            partido=partido+line.strip()
    if isEOF==False:
        game=list(partido)
        result=status(game)
        output(result,caseCounter)
        caseCounter=caseCounter+1
f.close()