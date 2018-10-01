lenCount = 3
wordCount = 5
vocab = ["abc","bca","dac","dbc","cba"]
alien = ["(ab)(bc)(ca)","abc","(abc)(abc)(abc)","(zyx)bc"]
import sys

inFile = open(sys.argv[1],"r")
outFile = open("output1","w")

inpNum = inFile.readline()
inpArr = inpNum.split()
lenCount = int(inpArr[0])
wordCount = int(inpArr[1])
alienCount = int(inpArr[2])

vocab =[]
alien = []
for i in range(wordCount):
    vocab.append(inFile.readline().rstrip())
for i in range(alienCount):
    alien.append(inFile.readline().rstrip())

mat = []
for i in range(wordCount):
    stri = vocab[i]
    subMat = []
    for j in range(lenCount):
        subMat.append(stri[j])
    mat.append(subMat)
    
import copy

numInp = 0
for tranStr in alien:
    numInp = numInp + 1
    matNew = copy.deepcopy(mat)
    i = 0
    j = 0
    while i<len(tranStr):
        if tranStr[i]=="(":
            while tranStr[i]!=")":
                for k in range(wordCount):
                    if matNew[k][j]==tranStr[i]:
                        matNew[k][j]="0"
                i = i + 1
            j = j+1
            i = i+1
        else:
            for k in range(wordCount):
	        if matNew[k][j]==tranStr[i]:
	            matNew[k][j]="0"
            i = i + 1
            j = j + 1
            
    count = 0
    for i in range(wordCount):
        inDict = True
        for j in range(lenCount):
            if matNew[i][j]!="0":
                inDict = False
                break
        if inDict:
           count = count + 1
    outFile.write("Case #%d: %d\n" % (numInp,count,))
    
inFile.close()
outFile.close()
            