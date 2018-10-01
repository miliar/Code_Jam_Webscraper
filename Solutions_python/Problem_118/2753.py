import math
def main():
  fi = open('Input.txt')
  fo = open('Output.txt','w')
  T = int(fi.readline())
  for j in xrange(T):
    occurences = 0
    endPoint = fi.readline().split()
    list=[]
    for i in xrange(int(endPoint[0]),(int(endPoint[1])+1)):
      list.append(i)
    palinCheckList = checkFair(map(lambda x: str(x), list))
    for i in xrange(len(palinCheckList)):
      if palinCheckList[i] == True:
        if checkSquare(int(list[i])) == True:
          if int(math.sqrt(int(list[i]))) == int(str(int(math.sqrt(int(list[i]))))[::-1]):
            occurences+=1
    fo.write('Case #'+str(j+1)+': '+str(occurences)+'\n')
  fi.close()
  fo.close()
        
def checkFair (list):
  palinBool = []
  for number in list:
    tempNum=''
    for i in xrange(len(number)-1, -1,-1):
      tempNum += number[i]
    if tempNum == number:
      palinBool.append(True)
    else:
      palinBool.append(False)
  return palinBool
      
      
def checkSquare(integer):
  root = math.sqrt(integer)
  if int(root + 0.5) ** 2 == integer: 
    return True
  else:
    return False


main()
