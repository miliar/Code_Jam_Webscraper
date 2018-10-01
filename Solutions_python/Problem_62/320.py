#!/usr/bin/python
# Filename: snapperchain.py

'''
Created on May 23, 2010

@author: zeest
'''

'''
Google Code Jam 2010
Round 1C 2010
URL: http://code.google.com/codejam
'''


'''

Problem Statement: Problem A

'''


#imports
from myFileIO import readFromFile, writeToFile

# File Paths

example1_in = 'example1.in'
example1_out = '/example1.out'

DEBUG = False
ASKFORFILE = True

def Pro1cA (inputFile, outputFile):    
    ''' Solves the problem.
    
    Elegantly '''
   
    fOK = True

    data = []
    results = []
    
    # read values
    data = readFromFile(inputFile)
    
    if len(data) <= 0:
        fOK = False
        
    if fOK:    
        TCases = int(data [0][0])
    
            
        if DEBUG:
            print data
            print TCases
        
        tStart = 1    
        # loop on test cases
        for t in range (0, TCases):
            # solve case
            Nwires = int(data[tStart][0])
            
            cStart = tStart+1
            cEnd = cStart+Nwires
            rCross = 0
            
            wires = data[cStart:cEnd]
            
            if DEBUG:
                print wires
            
            # loop on cables in this test cases
            for c in range (0, Nwires-1):
                lPos = int(wires[c][0])
                rPos = int(wires[c][1])
                
                lDiff = 0
                rDiff = 0
                
                
                if DEBUG:
                    #print "Number of Wires "+str(Nwires)+ "  Current wire: " +str(lPos) + " " + str(rPos)
                    print "Working line: " + str(c)
                    
                #compare with other cables
                for more in range (c+1, Nwires):
                    lPosThis = int(wires[more][0])
                    rPosThis = int(wires[more][1])
                    
                    lDiff = lPos - lPosThis
                    rDiff = rPos - rPosThis
                    
                    if DEBUG:
                        #print "Number of Wires "+str(Nwires)+ "  Current wire: " +str(lPosThis) + " " + str(rPosThis)
                        print "Comparing line: " + str(more)                        
                    
                    if not(((lDiff>=0) and (rDiff>=0)) or ((lDiff<=0) and (rDiff<=0))):
                        rCross = rCross +1
                #compare with other cables
            
            results.append(str(rCross))  
            # loop on cables in this test cases
            
            tStart = tStart + Nwires + 1 #next case is here
            # cases finished
                  
    if DEBUG:
        print results
        
    #output to file
    if len(results) > 0 and fOK :
        fOK = writeToFile(outputFile, results)
    
    return fOK              
# end of module                
            
            
if __name__ == "__main__":
    
    if ASKFORFILE:
        #input file paths
        inputFile = (raw_input('Enter input file path: '))
        outputFile = (raw_input('Enter output file path: '))
    else:
        inputFile = example1_in
        outputFile = example1_out
    
    if DEBUG:
        print inputFile
        print outputFile
    
    # solve the problem    
    fOK = Pro1cA(inputFile, outputFile)
    
    if fOK:    
        print "Successfully completed. Check the file at \r" + outputFile
    else:
        print "Error. Some problem with input file at \r" + inputFile
                