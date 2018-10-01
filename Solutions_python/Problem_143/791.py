def findNum(a, b, k):
  count = 0
  for i in range(b):
    for j in range(a):
      ans = i & j
      if ans < k:
        count += 1
  return count

fileIn = open("B-small-attempt0.in", 'r')
fileOut = open("bfile.out", 'w')
tCases = int(fileIn.readline())
curCase = 0
while tCases > curCase :
  op = 'Case #' + str(curCase + 1) + ': '
  val = [int(i) for i in fileIn.readline().split(' ')]
  k = findNum(val[0], val[1], val[2])
  op += str(k) + '\n'
  fileOut.write(op)
  curCase += 1
fileIn.close()
fileOut.close()
