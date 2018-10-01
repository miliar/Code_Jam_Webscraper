import sys
import heapq

def serializeInputFile(inputFile):
    inputList=[]
    f=open(inputFile)
    length=int(f.readline())
    while length>0:
        li = f.readline().split()
        strLen=int(li[0])
        repeatition=int(li[1])
        inputList.append( f.readline().rstrip() * repeatition )
        length-=1
    return inputList

def createOutputFile(outputFile,outputList):
    f=open(outputFile,"w")
    for index in range(len(outputList)):
        f.write("Case #" + str(index+1) + ": " + str(outputList[index]) + "\n")

def getTableValue(ch1,ch2):
    output=""
    prefix=""
    if (len(ch1) != len(ch2)):
        prefix = "-"
    ch1=ch1[-1]
    ch2=ch2[-1]
    if(ch1 == "1"):
        output = ch2
    if(ch2=="1"):
        output = ch1
    if(ch1==ch2):
        output = "-1"
    if(ch1=="i" and ch2=="j"):
        output = "k"
    if(ch1=="i" and ch2=="k"):
        output = "-j"
    if(ch1=="j" and ch2=="i"):
        output = "-k"
    if(ch1=="j" and ch2=="k"):
        output = "i"
    if(ch1=="k" and ch2=="i"):
        output = "j"
    if(ch1=="k" and ch2=="j"):
        output = "-i"
    if prefix == "":
        return output
    elif(len(output) == 2): #negative
        return output[-1]
    else:
        return (prefix + output)

"""
def search(li, findLi):
    start_1=0
    li_1=list(li)
    temp=0
    while(start_1<len(li_1)):
        start_2=find(li_1,start_1,findLi[0])
        li_2=list(li)
        while(start_2<len(li)):
            start_3=find(li_2,start_2,findLi[1])
            li_3=list(li)
            while(start_3<len(li)):
                end=find(li_3,start_3,findLi[2])
                if(end == len(li)):
                    return True
                start_3+=1
                if(start_3>=len(li)):
                    temp=li_3[-1]
                    if(getTableValue('j',temp)!="i"):
                        return False
            start_2+=1
            if (start_2>=len(li)):
                temp=li_2[-1]
                if(getTableValue("i",temp)!="-1"):
                    return False
        start_1+=1
    return False

def find(inputLi, start, sym):
    if start>=len(inputLi):
        return len(inputLi) + 1
    if (inputLi[start] == sym):
        if (len(inputLi) > start+1):
            inputLi[start + 1]=getTableValue(inputLi[start],inputLi[start + 1])
        return start + 1
    elif (len(inputLi) <= start+1):
        return len(inputLi) + 1
    else:
        inputLi[start + 1]=getTableValue(inputLi[start],inputLi[start + 1])
        return len(inputLi) + 1
"""

def search(li,ignore):
    d={}
    d["i"] = []
    d["k"] = []
    for index in range(len(li) - 1):
        if li[index] == "i": # Finding i
            d["i"].append(index)
        elif li[index] == "k": # Findin j i.e i * j = k
            d["k"].append(index)
        li[index + 1 ] = getTableValue(li[index] , li[index + 1])
    if li[len(li) - 1] != "-1" or d["i"] == [] or d["k"] == []:
        return False
    if d["i"][0] < d["k"][-1]:
        return True
    else:
        return False

inputFile=r"C:\Users\jaias_000\Desktop\C-small-attempt1.in"
#inputFile=r"C:\Users\jaias_000\Desktop\input.txt"
outputFile=r"C:\Users\jaias_000\Desktop\output.txt"
inputList = serializeInputFile(inputFile)
outputList=[]

"""
print search(["i","j","k"],["i","j","k"])
print search(["i","j","i","j"], ["i","j","k"])
print search(["j","i","j","i","j","i","j","i","j","i","j"], ["i","j","k"])
print search(["j","i","j","i","j","i","j","i","j","i","j","i"], ["i","j","k"])
print search(["j","i","j","i","j","i","j","i","j","i","j","i","k","-k"], ["i","j","k"])
print inputList
print getTableValue("1","1"), getTableValue("1","i"), getTableV1alue("1","j"), getTableValue("1","k")
print getTableValue("i","1"), getTableValue("i","i"), getTableValue("i","j"), getTableValue("i","k")
print getTableValue("j","1"), getTableValue("j","i"), getTableValue("j","j"), getTableValue("j","k")
print getTableValue("k","1"), getTab leValue("k","i"), getTableValue("k","j"), getTableValue("k","k")
"""
for data in inputList:
    data=list(data)
    outputList.append(["NO","YES"][search(data,["i","j","k"])])

createOutputFile(outputFile,outputList)