#!/usr/bin/python
import sys
import operator
from operator import itemgetter
dataX = []
dataO = []
if len(sys.argv)>1:
  infi = sys.argv[1]
  dataDX = []
  dataDO = []
  fi = open(infi)
  lines = fi.readlines()
  d = 0
  for line in lines:
    if len(line)<2:
      dataX.append(dataDX)
      dataO.append(dataDO)
      dataDX = []
      dataDO = []
    #print line,len(li)
    strtmp = line.replace("\n","")
    if d!=0 and len(line)>2:
      lX = []
      lO = []
      xline = strtmp.replace("T","X")
      oline = strtmp.replace("T","O")
      lX.extend(xline)
      lO.extend(oline)
      dataDX.append(lX)
      dataDO.append(lO)
    d+=1
  dataX.append(dataDX)
  dataO.append(dataDO)
c = 0
while c < len(dataX):
 win=False
 datan = dataX[c]
 if(datan[0][0]==datan[0][1]==datan[0][2]==datan[0][3]!='.'):
  win= datan[0][0]
 elif(datan[1][0]==datan[1][1]==datan[1][2]==datan[1][3]!='.'):
  win= datan[1][0]
 elif(datan[2][0]==datan[2][1]==datan[2][2]==datan[2][3]!='.'):
  win= datan[2][0]
 elif(datan[3][0]==datan[3][1]==datan[3][2]==datan[3][3]!='.'):
  win= datan[3][0]
 elif(datan[0][0]==datan[1][0]==datan[2][0]==datan[3][0]!='.'):
  win= datan[0][0]
 elif(datan[0][1]==datan[1][1]==datan[2][1]==datan[3][1]!='.'):
  win= datan[0][1]
 elif(datan[0][2]==datan[1][2]==datan[2][2]==datan[3][2]!='.'):
  win= datan[0][2]
 elif(datan[0][3]==datan[1][3]==datan[2][3]==datan[3][3]!='.'):
  win= datan[0][3]
 elif(datan[0][0]==datan[1][1]==datan[2][2]==datan[3][3]!='.'):
  win= datan[0][0]
 elif(datan[0][3]==datan[1][2]==datan[2][1]==datan[3][0]!='.'):
  win= datan[0][3]
 if win==False:
   datan = dataO[c]
   if(datan[0][0]==datan[0][1]==datan[0][2]==datan[0][3]!='.'):
    win= datan[0][0]
   elif(datan[1][0]==datan[1][1]==datan[1][2]==datan[1][3]!='.'):
    win= datan[1][0]
   elif(datan[2][0]==datan[2][1]==datan[2][2]==datan[2][3]!='.'):
    win= datan[2][0]
   elif(datan[3][0]==datan[3][1]==datan[3][2]==datan[3][3]!='.'):
    win= datan[3][0]
   elif(datan[0][0]==datan[1][0]==datan[2][0]==datan[3][0]!='.'):
    win= datan[0][0]
   elif(datan[0][1]==datan[1][1]==datan[2][1]==datan[3][1]!='.'):
    win= datan[0][1]
   elif(datan[0][2]==datan[1][2]==datan[2][2]==datan[3][2]!='.'):
    win= datan[0][2]
   elif(datan[0][3]==datan[1][3]==datan[2][3]==datan[3][3]!='.'):
    win= datan[0][3]
   elif(datan[0][0]==datan[1][1]==datan[2][2]==datan[3][3]!='.'):
    win= datan[0][0]
   elif(datan[0][3]==datan[1][2]==datan[2][1]==datan[3][0]!='.'):
    win= datan[0][3]
 if (win==False and ('.' in datan[0] or '.' in datan[1] or '.' in datan[2] or '.' in datan[3])):
   win = True
 if win==False:
   print "Case #"+str(c+1)+": Draw"
 elif win==True:
   print "Case #"+str(c+1)+": Game has not completed"
 else:
   print "Case #"+str(c+1)+": "+win+" won"
 c+=1
