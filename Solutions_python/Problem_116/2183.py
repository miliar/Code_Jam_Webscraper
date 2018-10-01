import string



def oyunIncele(f,case,f2):
    x=[]
    for i in range(4):
        line=f.readline().splitlines()
        line=list(line[0])
        x.append(line)      
    f.readline()
##    print x

    

            
    # x ekseninde oyun tamamlanmis mi bak
    for i in range(4):
        countO=0
        countX=0
        for j in range(4):
                # o ya bak
                if x[i][j]== "O" or x[i][j] == "T":
                        countO+=1
                if countO==4:
                        print >>f2, "Case #"+str(case)+": O won"
                        return
                
                # x e bak
                if x[i][j]== "X" or x[i][j] == "T":
                        countX+=1
                if countX==4:
                        print >>f2, "Case #"+str(case)+": X won"
                        return

    # y ekseninde oyun tamamlanmis mi bak
    for j in range(4):
        countO=0
        countX=0
        for i in range(4):
                # o ya bak
                if x[i][j]== "O" or x[i][j] == "T":
                        countO+=1
                if countO==4:
                        print >>f2, "Case #"+str(case)+": O won"
                        return
                
                # x e bak
                if x[i][j]== "X" or x[i][j] == "T":
                        countX+=1
                if countX==4:
                        print >>f2, "Case #"+str(case)+": X won"
                        return
                
    # diyagonal oyun tamamlanmis mi bak
    countO=0
    countX=0
    for j in range(4):

        # o ya bak
        if x[j][j]== "O" or x[j][j] == "T":
                countO+=1
        if countO==4:
                print >>f2, "Case #"+str(case)+": O won"
                return
                
        # x e bak
        if x[j][j]== "X" or x[j][j] == "T":
                countX+=1
        if countX==4:
                print >>f2, "Case #"+str(case)+": X won"
                return

    countO=0
    countX=0
    for j,i in zip(range(4),reversed(range(4))):

        # o ya bak
        if x[j][i]== "O" or x[j][i] == "T":
                countO+=1
        if countO==4:
                print >>f2, "Case #"+str(case)+": O won"
                return
                
        # x e bak
        if x[j][i]== "X" or x[j][i] == "T":
                countX+=1
        if countX==4:
                print >>f2, "Case #"+str(case)+": X won"
                return
    

    #oyun bitmis mi?
    for a in range(4):
        i = ''.join(x[a])
        for j in i:
            if j == ".":
                print >>f2, "Case #"+ str(case) +": Game has not completed"
                return

    # drawn
    print >>f2, "Case #"+ str(case) +": Draw"
    return


def main():
    f = open('A-large.in')
    f2 = open('A-large.out','w+')
    #case oku
    lines = f.readline()
    case = int(lines)


    for i in range(case):
        oyunIncele(f,i+1,f2)


main()
        



