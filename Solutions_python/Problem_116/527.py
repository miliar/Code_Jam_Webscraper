import sys

def checkResult(r):
  if r&1<<0 or r&1<<2 or r&1<<5 or r&1<<7:
    return "X won"
  elif r&1<<1 or r&1<<3 or r&1<<6 or r&1<<8:
    return "O won"
  elif r&1<<4:
    return "Draw"
  else:
    return "Game has not completed"

def statusGame(data):
  r = 0b11111
  for i in range(4):
    if data[i][i] == 'X':
      r = r & ~(1<<1)
    elif data[i][i] == 'O':
      r = r & ~(1<<0)
    elif data[i][i] == '.':
      r = r & ~(1<<0 | 1<<1)
    
    if data[i][3-i] == 'X':
      r = r & ~(1<<3)
    elif data[i][3-i] == 'O':
      r = r & ~(1<<2)
    elif data[i][3-i] == '.':
      r = r & ~(1<<2 | 1<<3)
  ret = checkResult(r)
  if ret in ('X won','O won'):
    return ret    
  for i in range(4):
    r = r | (0b1111<<5)  
    for j in range(4):
      if data[i][j] == 'X':
        r = r & ~(1<<6)
      elif data[i][j] == 'O':
        r = r & ~(1<<5)
      elif data[i][j] == '.':
        r = r & ~(1<<5 | 1<<6)
        r = r & ~(1<<4)
      if data[j][i] == 'X':
        r = r & ~(1<<8)
      elif data[j][i] == 'O':
        r = r & ~(1<<7)
      elif data[j][i] == '.':
        r = r & ~(1<<7 | 1<<8)
    ret = checkResult(r)
    if ret in ('X won','O won'):
      return ret
  return checkResult(r)

def main():
  inputFile = open('A-large.in','r')
  outputFile = open('A-large.txt','w')
  index = 0
  for inputLine in inputFile:
    currLine = index%5
    if currLine == 1:
      inputData = [['.']*4 for i in range(4)]
      inputData[currLine-1] = [x for x in inputLine[:4]]
    elif currLine == 0 and index == 0:
      T = int(inputLine)
      caseNum = 0
    elif currLine == 0:
      result = statusGame(inputData)
      caseNum += 1
      outputStr = 'Case #' + str(caseNum) + ': ' + result + '\n'
      outputFile.write(outputStr)
    else:
      inputData[currLine-1] = [x for x in inputLine[:4]]
    index += 1
  inputFile.close()
  outputFile.close()

if __name__ == '__main__':
  main()