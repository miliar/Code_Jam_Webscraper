'''
Bot Trust
'''
def readInFile(path):
    t = 0
    with open(path,"r") as f:
        t =  int(f.readline())

        lines = f.readlines()
    return t,lines


def writeOutFile(path,data):
    with open(path,"w") as f:
        for i in range(len(data)):
            f.write("Case" + " #"+str(i+1) + ": " +str(data[i]) + "\n")

    
def solve(data):
    results = []
    
    
    for line in data[1]:
        #n = int(line[0])
        print 'line : ' ,line
        
        opos = 1
        bpos = 1
        
        buttons = line.replace('\n','').split(' ')
        buttons = buttons[1:]
        movesList = []
        omovesList=[]
        bmovesList=[]
        for i in range (0,len(buttons),2):
            print buttons,i
            move1 = buttons[i] + buttons[i+1]
            movesList.append(move1)
            
            if move1[0] == 'O' : omovesList.append(move1)
            elif move1[0] == 'B' : bmovesList.append(move1)

        
        #movesList.reverse()
        #omovesList.reverse()
        #bmovesList.reverse()
        m = 0
        while movesList:
            
            botsTurn = movesList[0][0]
            newopos = 0
            newbpos = 0
            if omovesList :                 
                newopos = int(omovesList[0][1:])
            if bmovesList :                 
               newbpos =  int(bmovesList[0][1:])
            
            binplace = False
            oinplace = False
            
            
            
            #Orange
            if opos < newopos : opos +=1
            elif opos > newopos : opos -=1
            else :oinplace = True
            
            
            #Blue
            if bpos < newbpos : bpos +=1
            elif bpos > newbpos : bpos -=1
            else :binplace = True
            
            if botsTurn == 'O':
                if oinplace : 
                    movesList.remove(movesList[0])
                    omovesList.remove(omovesList[0])
                    
            
            if botsTurn == 'B':
                if binplace : 
                    movesList.remove(movesList[0])
                    bmovesList.remove(bmovesList[0])
            
            m+=1
        results.append(m)
    return results

def main():
    data = readInFile("A-large.in")
    results = solve(data)
    writeOutFile("A-large.out",results)
    print "Done."
    print results


if __name__ == '__main__':
    main()