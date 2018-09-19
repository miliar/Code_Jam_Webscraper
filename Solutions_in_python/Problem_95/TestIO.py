'''
Created on Apr 13, 2012

@author: Jay
'''
myFile = "C:\\Users\\Jay\\Desktop\\test.txt"
input = "C:\\Users\\Jay\\Desktop\\test2.txt"

#build dictionary
f = open(myFile, "r")
fout = open("C:\\Users\\Jay\\Desktop\\testOut.txt", "w")

mydict = dict({'y':'a', 'e':'o', 'q':'z', 'z':'q'})
for i in range(3):
    firstLine = f.readline()
    secondLine = f.readline()
    
    #read through each line and store in dictionary
    for k in range(len(firstLine)):
        mydict[firstLine[k]] = secondLine[k]
        
f = open(input, "r")
numLines = int(f.readline())
casenum = 0
for line in f:
    myString = ""
    for i in line:
        myString += mydict[i]
    casenum +=1
    tmpstr = 'Case #'+str(casenum)+': '+myString
    fout.write(tmpstr)
    
fout.close()

for i in range(97,123):
    print chr(i)+": "+mydict[chr(i)]