def countMoney(R,K,G):
    money=0
    for i in range(R):
        roller=0
        count=0
        while (roller+G[0])<=K :

            roller+=G[0]
            G.append(G.pop(0))
            count+=1
            if len(G)==1 or count==(len(G)): break
            
        money+=roller
            
    return money
    

def main():

    fileIn = open("in.in")
    fileOut = open("out.out","w")

    lines = fileIn.read().split("\n")
    fileIndex = 0
    nCase = int(lines[fileIndex])
    fileIndex+=1

    for case in range(nCase):
        line = lines[fileIndex].split(" ")
        fileIndex+=1
        
        R = int(line[0])
        K = int(line[1])
        N = int(line[2])

        line = lines[fileIndex].split(" ")
        fileIndex+=1

        for i in range(len(line)):
            line[i] = int(line[i])

        
       # fileOut.write(str(R)+" "+str(K)+" "+str(line)+"\n")
        fileOut.write("Case #"+str(case+1)+": "+str(countMoney(R,K,line))+"\n")


    fileIn.close()
    fileOut.close()


main()

#print(countMoney(4, 10, [1 ,4 ,2 ,1]))
