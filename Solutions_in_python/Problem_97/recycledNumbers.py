
import re


def findPermu(strI):
    for i in range(len(strI)):
        strT = strI[-1-i:] + strI[:-1-i]
        if strT == strI or strT[0] == '0' or int(strT) < firstNum or int(strT) > secondNum or int(strT) in numMap[int(strI)]:
            continue
        else:
            numMap[int(strI)].append(strT)

fileIn= open("/home/rahul/Documents/codeJam2012/C-small-attempt0.in",  "r")
fileOut = open("/home/rahul/Documents/codeJam2012/C-small-attempt0.out", "w") 
 
#fileIn= open("/tmp/input.txt",  "r")
#fileOut= open("/tmp/output.txt",  "w")

n = int(fileIn.readline())

for i in range(n):
    line = fileIn.readline()
    resLine = 'Case #' + str(i+1) + ': '
            
    lineList = re.split('\s+',  line)
    firstStr = lineList[0]
    secondStr = lineList[1]
    firstNum = int(firstStr)
    secondNum = int(secondStr)
    numMap = {}
    for i in range(firstNum,  secondNum+1):
        numMap[i] = []
        findPermu(str(i))
    
    totalComb = 0
    for itemList in numMap.itervalues():
        totalComb += len(itemList)
   
     
  
    res = totalComb / 2
    st = ''
    if line[-1] == '\n':
        st = '\n'
    fileOut.write(resLine + str(res) + st) 

fileIn.close()
fileOut.close()

