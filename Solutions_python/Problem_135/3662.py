
f = open('A-small-attempt0.in', 'r')
fw = open('result.txt', 'w')
numTest = int(f.readline())
for i in range(numTest):
  ansA = int(f.readline())
  arrayA = []
  for j in range(4):
    line = f.readline().split()
    if j == ansA - 1:
      arrayA = line
  ansB = int(f.readline())
  arrayB = []
  for j in range(4):
    line = f.readline().split()
    if j == ansB - 1:
      arrayB = line
  ans = ''
  for j in range(4):
    for k in range(4):
      if arrayA[j] == arrayB[k]:
        if ans == '':
          ans = arrayA[j]
        else:
          ans = 'Bad magician!'
        break

  if ans == '':
    ans = 'Volunteer cheated!'
  fw.write('Case #' + str(i+1) + ': ' + ans + '\n')
fw.close()

