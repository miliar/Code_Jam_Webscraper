import glob, time, string, re
textFile = open("A-output_small.txt", "w")
#textFile = open("A-output_large.txt", "w")
#open and read the input file
sInputFileLoc = 'A-small-attempt0.in'
#sInputFileLoc = 'A-large-practice.txt'
sInputFile = open(sInputFileLoc, "r")
sLineOutput = "Case #"
iLineRead = 0

iNumTestCases = int(sInputFile.readline())

sBefore   = ['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q',' ','\n']
sKeyArray = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','\n']


for x in range(iNumTestCases):
    sInputString = sInputFile.readline()
    sTemp = ""
    sTempLast = ""
    textFile.write(sLineOutput+str(x+1)+ ": ")    
    for letter in sInputString:
        sTempLast = str(sKeyArray[ sBefore.index( letter )])[:1]
        sTemp = sTemp + str(( sKeyArray[ sBefore.index( letter ) ]))

    textFile.write(sTemp)
    sTempLast = ""

    textFile.write("\n")    
textFile.close()
sInputFile.close()
