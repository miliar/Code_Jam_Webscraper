import csv #Flexible File Reading

def loadInput(theFile):
    fileReader = csv.reader(open(theFile),delimiter=" ")
    #Ignore First Line as we just iterate through
    idx = 0
    outFile = open("snapper-Large.out","w")
    for line in fileReader:
        if idx == 0:
            print "Skipping"
            pass
        else:
            out = runTest(line)
            outStr = "OFF"
            if out:
                outStr = "ON"
            outStr = "Case #%s: %s" %(idx,outStr)
            outFile.write("%s\n" %outStr)
            print outStr
            
        idx += 1

    outFile.close()
    

def runTest(inVals):
    n = int(inVals[0])
    k = int(inVals[1])
    #print n,k
    #Convert N to Binary Represenstation
    binVal = 2**n
    #print "BIN REP ",binVal
    #Catch Varous Corner Cases
    if k == 0:
        return False
    elif n == 1 and k == 1:
        return True
    else:
        #Otherwise (K + 1) % Binary represention should give On / Off
        #print (k + 1) % binVal
        return (k + 1) % binVal  == 0
    
    
    

if __name__ == "__main__":
    #loadInput("A-small-attempt1.in")
    loadInput("A-large.in")
    
    
    
        


        
