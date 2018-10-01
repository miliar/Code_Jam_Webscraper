'''
Created on 08.05.2010

@author: Dong Li
'''

def getResult(times,capacity,Groups):
    peopleCount=0
    sum=0
    resultsDict=dict()
    keySequence=[]

    for i in range(times):
        key=Groups[0][0]
        #print key
        if key in resultsDict:
            firstRestSum=0
            firstRestIndex=keySequence.index(key)
            if firstRestIndex>0:
                for k in keySequence[0:firstRestIndex]:
                    firstRestSum+=resultsDict[k]
            loopSequence=keySequence[firstRestIndex:]
            sequenceSum=sum-firstRestSum
            multiple=(times-firstRestIndex)/len(loopSequence)
            rest=(times-firstRestIndex)%len(loopSequence)
            restSum=0
            for k in range(rest):
                restSum=restSum+resultsDict[loopSequence[k]]
            sum=sequenceSum*multiple+restSum+firstRestSum
            return sum
            #print resultsDict[key]
        else:
            playingPeople=[]
            peopleCount=0
            while len(Groups)!=0:
                tmpsum=peopleCount+Groups[0][1]
                if tmpsum>capacity:
                    break
                else:
                    peopleCount=tmpsum
                    playingPeople.append(Groups.pop(0))

            if len(Groups)==0:
                return times*peopleCount
            sum+=peopleCount
            resultsDict[key]=peopleCount
            keySequence.append(key)
            #print playingPeople
            Groups.extend(playingPeople)
            #print Groups
        #print Groups

    return sum


inputFile="C-large.in"
outputFile=open(inputFile.split(".")[0]+".out",'w')
input=open(inputFile)

R=0
K=0
N=0
caseNum=0
lineCount=0
for line in input:
    if lineCount==0:
        caseNum=int(line)
        lineCount+=1
    elif lineCount%2==1:
        rkn=line.split()
        R=int(rkn[0])
        K=int(rkn[1])
        N=int(rkn[2])
        lineCount+=1
    elif lineCount%2==0:
        str_groups=line.split()
        Groups=[]
        count=0
        for group in str_groups:
            count+=1
            Groups.append((count,int(group)))
        #print R,K,Groups
        result="Case #"+str(lineCount/2)+": "+str(getResult(R,K,Groups))
        #print result
        lineCount+=1
        outputFile.write(result+"\n")

input.close()
outputFile.close()














