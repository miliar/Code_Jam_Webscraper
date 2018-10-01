import string
import math
def readFile():
  triggerfile = open("C-small-attempt0.in", "r")
  all = [ line.rstrip() for line in triggerfile.readlines() ]
  lines=[]
  for line in all:
    lines.append(line.split(' '))
  return lines
def isPalinDrome(number):
  temp=''
  count=len(str(number))
  while(count!=0):
    count-=1
    temp=temp+str(number)[count]
  return str(temp)==str(number)
  
def isFairAndSquare(number):
  x=math.sqrt(number)
  return isPalinDrome(number) and isPalinDrome(int(x)) and int(x)**2==number

def numFAS(start, end):
  numfas=0
  for i in range(int(start), int(end+1)):
    if isFairAndSquare(i):
      numfas+=1
  return numfas
lines=readFile()
x=int(lines[0][0]) #x is number of cases
lines.remove(lines[0]) #now lines is list of lists
file1=open('outputsmall','w') #make a blank file
for i in range(x):
  output= 'Case #'+str(i+1)+': '+str(numFAS(int(lines[i][0]),int(lines[i][1])))
  file1=open('outputsmall','a') #open file
  file1.write(output+'\n') #write to file
  file1.close()            #close the file
  print output