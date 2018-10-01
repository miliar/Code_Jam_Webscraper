
def num_ge_p(caseNum, splitData):
    contestCount = int(splitData[0])
    surpriseTripCount = int(splitData[1])
    bestResComp = int(splitData[2])
    ge_p_count = 0
    #go through each contestant total score for a given line
    for x in range(3,(contestCount+3)):
        total = int(splitData[x])
        a = total/3
        b = (total-a)/2
        c = total-(a+b)

        if c >= bestResComp:
            ge_p_count += 1
        elif ((surpriseTripCount != 0) and (b==c) and (a!=0)):
            if ((c+1) >= bestResComp):
                surpriseTripCount -= 1
                ge_p_count += 1
                if ((a==b)and(b==c)):
                    c += 1
                    a -= 1
                elif ((a<b)and(b==c)):
                    c += 1
                    b -=1
         
    return "Case #%d: %d" % ((caseNum+1),ge_p_count) 

def main():
    inputFile = open("/home/brenton/Development/codeJam/dancing/input", 'r')
    outputFile = open("/home/brenton/Development/codeJam/dancing/output", 'w')

    numLines = inputFile.readline()
    numLines = int(numLines[0:(len(numLines)-1)])

    for x in range(numLines):
        data = inputFile.readline()
        dataSplit = data.split()
        outputFile.write(num_ge_p(x,dataSplit)+'\n')

if __name__=="__main__":
    main()
