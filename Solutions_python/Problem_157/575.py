import time
#import math
#import sys
#import fractions

debug = True
inFile = "C-small-attempt1.in"
outFile = inFile.rstrip(".in") + ".out"

qMultTable = {'1':{'1':"1", 'i':"i", 'j':"j", 'k':"k", '-1':"-1", '-i':"-i", '-j':"-j", '-k':"-k"},
              'i':{'1':"i", 'i':"-1", 'j':"k", 'k':"-j", '-1':"-i", '-i':"1", '-j':"-k", '-k':"j"},
              'j':{'1':"j", 'i':"-k", 'j':"-1", 'k':"i", '-1':"-j", '-i':"k", '-j':"1", '-k':"-i"},
              'k':{'1':"k", 'i':"j", 'j':"-i", 'k':"-1", '-1':"-k", '-i':"-j", '-j':"i", '-k':"1"},
              '-1':{'1':"-1", 'i':"-i", 'j':"-j", 'k':"-k", '-1':"1", '-i':"i", '-j':"j", '-k':"k"},
              '-i':{'1':"-i", 'i':"1", 'j':"-k", 'k':"j", '-1':"i", '-i':"-1", '-j':"k", '-k':"-j"},
              '-j':{'1':"-j", 'i':"k", 'j':"1", 'k':"-i", '-1':"j", '-i':"-k", '-j':"-1", '-k':"i"},
              '-k':{'1':"-k", 'i':"-j", 'j':"i", 'k':"1", '-1':"k", '-i':"j", '-j':"-i", '-k':"-1"}}

qDivTable = {'1':{},'i':{},'j':{},'k':{},'-1':{},'-i':{},'-j':{},'-k':{}}

def populateQDivTable():
    for r,t in qMultTable.items():
        for c,v in t.items():
            qDivTable[v][r] = c

def qMult(left, right):
    
    return qMultTable[left][right]
    

def dijkstra(testNum, fin):
    dbgPrint("")
    
    dbgPrint("Test %d" % testNum)
    dbgPrint("----------")
    
    numLetters,numRepeat = fin.readline().rstrip("\n").split(" ")
    numLetters = int(numLetters)
    numRepeat = int(numRepeat)
    dbgPrint("numLetters = %d   numRepeat = %d" % (numLetters,numRepeat))
    
    letters = fin.readline().rstrip("\n")
    #dbgPrint("letters = %s" % (letters))
    
    theString = letters * numRepeat
    
    #dbgPrint(theString)
    
    if len(theString) < 3:
        return "NO"
    
    moreThan1 = 0
    moreThan1 += 1 if "i" in letters else 0
    moreThan1 += 1 if "j" in letters else 0
    moreThan1 += 1 if "k" in letters else 0
    
    if moreThan1 == 1:
        return "NO"
    
    letterRepeatBlockCnt = 1
    letterRepeatBlockLen = len(letters)
    for x in reversed(range(2,(len(letters)/2)+1)):
        if len(letters) % x == 0:
            tstStr = letters[0:int(len(letters)/x)]
            if letters == tstStr*x:
                letterRepeatBlockCnt = x
                letterRepeatBlockLen = len(letters)/letterRepeatBlockCnt
                break
    
    letterRepeatBlockCnt *= numRepeat
    dbgPrint("letterRepeatBlockLen = %d" % (letterRepeatBlockLen))
    dbgPrint("letterRepeatBlockCnt = %d" % (letterRepeatBlockCnt))
    
    outputRepeatBlockLen = 0
    loopBuffer = [theString[0]]
    for x in range(1, len(theString)):
        n = qMultTable[loopBuffer[-1]][theString[x]]
        loopBuffer.append(n)
        if (x+1) % letterRepeatBlockLen == 0 and n == "1":
            outputRepeatBlockLen = x+1
            break
    
    dbgPrint("outputRepeatBlockLen = %d" % (outputRepeatBlockLen))
    #dbgPrint(loopBuffer)
    
    if "i" not in loopBuffer:
        return "NO"
    
    if outputRepeatBlockLen == 0 or outputRepeatBlockLen > len(theString)-2:
        outputRepeatBlockLen = len(theString)-2
        
    ibuffer = "1"
    #dbgPrint("ibuffer")
    for i in range(outputRepeatBlockLen):
        ibuffer = qMultTable[ibuffer][theString[i]]
        if ibuffer == "i":
            #dbgPrint("i = %d  --  letter = %s  --  now ibuffer = %s" % (i,theString[i],ibuffer))
            jbuffer = theString[i+1]
            kbuffer = "1"
            for k in range(i+2, len(theString)):
                kbuffer = qMultTable[kbuffer][theString[k]]
            if jbuffer == "j" and kbuffer == "k":
                return "YES"
            for x in range(i+2, len(theString)):
                jbuffer = qMultTable[jbuffer][theString[x]]
                kbuffer = qDivTable[kbuffer][theString[x]]
                #dbgPrint("j = %d  --  letter = %s  --  now jbuffer = %s" % (j,theString[j],jbuffer))
                if jbuffer == "j" and kbuffer == "k":
                    return "YES"
                elif jbuffer == "1" and (x-i) % outputRepeatBlockLen == 0:
                    break
    
    return "NO"

def dbgPrint(string):
    if debug:
        print(string)

def go():
    fin = open(inFile, "rU")
    fout = open(outFile, "w")
    
    numTests = int(fin.readline())
    print("Number of tests = %d" % numTests)
    
    ts = time.clock()
    
    for testNum in range(1,numTests+1):
        s = time.clock()
        answer = dijkstra(testNum, fin)
        outStr = "Case #%d: %s" % (testNum, answer)
        print("%s" % outStr)
        fout.write("%s\n" % outStr)
        e = time.clock() - s
        print("time = %s" % (e))
        
    te = time.clock() - ts
    print("Total time = %s" % (te))
    
    fout.close()
    fin.close()

if __name__ == "__main__":
    populateQDivTable()
    go()
