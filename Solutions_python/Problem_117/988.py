from math import *
import random

def loadLawn(fileName,numRows):
    """retruns the array of arrays, and chews through the number of lines
"""
    lawn=[]
    for rowNo in range(0,numRows):
        rowArray=fileName.readline().strip().split(" ")
        lawn.append(rowArray)
    return lawn

def getCol(lawnArray,ColNum):
    newarray=[]
    for row in lawnArray: #Going down
        newarray.append(row[ColNum])
        
    return newarray

def arrayToInts(array):
    """Turns an array of strings into an array of ints"""
    return [int(x) for x in array]

def possible(array,index):
    """if a position on an array is cuttable"""
    array=arrayToInts(array)

    if len(array)==1:
        return True
    height=array[index]
    array.pop(index) #Remaining
    return  height >= max(array)

    
        



#-----------------Main------------------------
                             
def lm(filename = "lm.in"):
    txt = open(filename, "rU")
    solution = open("solution.txt","w")
    #Read topline info
    topline=txt.readline()
    noCases = int(topline.strip())
    print "No of cases: " + str(noCases)


    #For each lawn:
    for case in range(1,noCases+1):
        data=txt.readline().strip().split(" ")
        numRows=int(data[0])
        colWidth=int(data[1])
        caseSoln='YES'
        
        #Load the lawn
        lawn=loadLawn(txt,numRows)

        #Check for minimals
        rowIndex=-1
        for row in lawn:
            rowIndex+=1
            
            for index in range(len(row)):
                if possible(row,index):
                    continue
                if possible(getCol(lawn,index),rowIndex):
                    continue #next index along
                caseSoln='NO'
                break
                
            if caseSoln=='NO':
                break

        solution.write("Case #"+str(case)+": " + caseSoln+"\n")


        
    txt.close()
    solution.close()
    print "Done"

    
