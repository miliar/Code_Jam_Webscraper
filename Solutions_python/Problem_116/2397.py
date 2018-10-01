import sys

def CheckCompleted(a,b,c,d):
  for line in (a,b,c,d):
    for char in line:
      if char == '.':
        return False
  return True

def CheckVictory(a,b,c,d):
  groups = [a,b,c,d]
  for i in range(4):
    groups.append(a[i] + b[i] + c[i] + d[i])
  groups.append(a[0] + b[1] + c[2] + d[3])
  groups.append(a[3] + b[2] + c[1] + d[0])
  for group in groups:
    if group in ('XXXX', 'XXXT', 'XXTX', 'XTXX', 'TXXX'):
      return 'X'
    if group in ('OOOO', 'OOOT', 'OOTO', 'OTOO', 'TOOO'):
      return 'O'
  return False


# Script
fptr = open(sys.argv[1], "r")
content = fptr.readlines()
boards = []
del content[0]
for case,i in enumerate(range(0, len(content)-1, 5)):
  victor =  CheckVictory(content[i].strip(), content[i+1].strip(), content[i+2].strip(), content[i+3].strip())
  if victor:
    result = victor + ' won'
  elif CheckCompleted(content[i].strip(), content[i+1].strip(), content[i+2].strip(), content[i+3].strip()) == True:
    result = 'Draw'
  else:
    result = 'Game has not completed'

  print 'Case #' + str(case+1) + ': ' + result
