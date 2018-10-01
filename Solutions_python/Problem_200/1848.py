import time
from twisted.web.test.test_flatten import HERE
from numpy import append

def reduce(x):
    numList = [int(i) for i in str(x)]
    #print numList
    listLen = len(numList)
    if listLen == 1:
        return numList
    for i in range(listLen-1,0,-1):
        if numList[i-1]>numList[i]:
            y = numList[:i]
            z = numList[i:]
            #replace 2nd half by 9s
            #print z
            for a,b in enumerate(z):
                z[a] = 9
            #print z
            half1 = int(''.join(map(str,y)))
            #print half1-1
            return reduce(half1-1)+z
            #reduce 1st half by 1
            #reduce 1st half and append
            #return that  
    return numList      

            

def fileRead():
    start = time.time()
    fo = open("input.txt", "rw+")
    lineList = fo.readlines()
    noTestCases = int(lineList[0])
    #print "No Test Cases : "+str(noTestCases)
    f = open('output.txt', 'w')
    for i in range(1, noTestCases+1):
        wordArray = []
        #print "Case #",i," : ",lineList[i]        
        lastTidyNumber = reduce(long(lineList[i]))
        print "Case #"+str(i)+": "+str(int(''.join(map(str,lastTidyNumber))))
        if(i==noTestCases):
            f.write("Case #"+str(i)+": "+str(int(''.join(map(str,lastTidyNumber)))))
        else:
            f.write("Case #"+str(i)+": "+str(int(''.join(map(str,lastTidyNumber))))+'\n')
    f.close()
    elapsed = (time.time() - start)
    print elapsed


def main():
    fileRead()

if __name__ == "__main__":
    main()
