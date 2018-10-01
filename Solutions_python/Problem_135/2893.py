# Read the corresponding row
# hash each element 
# check the elements of the other row against the hashed elements

fileIn = open("A-small-attempt4.in", 'r')
fileOut = open("file.out", 'w')
tCases = int(fileIn.readline())
curCase = 0
while tCases > curCase:
  op = ''
  fRow = int(fileIn.readline())
  elem = ''
  for i in range(4):
    if i == (fRow - 1):
      elem = fileIn.readline()
    else:
      fileIn.readline()
  elem = [int(i) for i in elem.split(' ')]
  sRow = int(fileIn.readline())
  for i in range(4):
    if (i + 1) == sRow:
      vals = fileIn.readline()
    else:
      fileIn.readline()
  vals = [int(i) for i in vals.split(' ')]
  count = 0
  for i in range(4):
    for j in range(4):
      if elem[i] == vals[j]:
        op = str(elem[i])
        count += 1
  if count > 1:
    op = 'Bad magician!'
  elif count == 0:
    op = 'Volunteer cheated!'
  fileOut.write("Case #" + str(curCase + 1) + ': ' + op + '\n')
  curCase += 1
