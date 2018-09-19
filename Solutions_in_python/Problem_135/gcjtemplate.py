#!/usr/bin/python
# -*- coding: utf-8 -*- 
import sys
import time

def getValue(inputFile,dataType="string"):
  line=""
  value=0
  while len(line) < 1:
    line=inputFile.readline()

  if dataType=="string":
    value=line.split()[0]
  elif dataType=="integer":
    value=int(line.split()[0])
  elif dataType=="float":
    value=float(line.split()[0])

  return value

def getList(inputFile,dataType="string",separator="space"):
  # dataType could be string, integer and float
  # separator can be space or none
  list=[]
  
  line=""
  while len(line) < 1:
    line=inputFile.readline()

    if  separator=="space":
      list=line.split()
    elif separator=="none":
      line=line.rstrip('\n')
      for i in range(len(line)):
        list.append(line[i])


  #if dataType=="string": ... already a string
  if dataType=="integer":
    i=0
    while i<len(list):
      list[i]=int(list[i])
      i=i+1
  elif dataType=="float":
    i=0
    while i<len(list):
      list[i]=float(list[i])
      i=i+1
  return list

def getBoard(inputFile,dimX,dimY,dataType="string",separator="none"):
  line=""
  board=[]
 
  for y in range(dimY):
      board.append(getList(inputFile,dataType,separator))
 
  return board

def printBoard(board,array="0"):
  #print board
  for i in range(len(board)):
    for j in range(len(board[i])):
      if array=="1":
        sys.stdout.write("[\""+str(board[i][j])+"\"]")
      else:
        sys.stdout.write(str(board[i][j]))
        
    print ""
  
### solve it! ###
def solveIt(inputs, values,board):
#  time.sleep(1)
#  print ""
#  print inputs
#  print values
#  print board

  res=[]
  i=0
  j=1

  res.append(i)
  res.append(j)

  return res

if __name__=='__main__':
  # Open input and output files
  inputFile=open(sys.argv[1],'r')
  outputFile=open(sys.argv[2],'w')

  # Get number of cases
  NoC=int(getValue(inputFile))

  # for each case
  for i in range(NoC):
    # get case data
    inputs=getValue(inputFile,"integer")
    values=getList(inputFile,"integer")
    board=getBoard(inputFile,"integer")
    # solve problem
    res=solveIt(inputs, values, board)

    # write data    
    outputFile.write("Case #"+str(i+1)+": "+str(res[0]+1)+" "+str(res[1]+1)+"\n")
#    print "Case #"+str(i+1)+": "+str(res[0]+1)+" "+str(res[1]+1)

  # Close input and output files
  inputFile.close()
  outputFile.close()
