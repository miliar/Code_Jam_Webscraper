import string
import re
import numpy as np

#print "**Code Jam Problem 1**"

foo = raw_input('Enter file name: ')
f = open(foo,'r')
data = f.readlines()

#print "Number of lines: " + str(int(data[0]))

numlines = int(data[0])
final = []

matrix = []
linecnt = 0

for i in xrange(1, (numlines*5)):
    datamat = []
    for j in xrange(len(data[i])-1):
        if(data[i][j] == 'X'):
            datamat.append(1)
        if(data[i][j] == 'O'):
            datamat.append(2)
        if(data[i][j] == '.'):
            datamat.append(0)
        if(data[i][j] == 'T'):
            datamat.append(3)

    matrix.append(datamat)

finalmat = []
cnt = 0

for i in xrange(numlines):
    finalmat.append([])
for i in xrange(0, numlines):
    finalmat[i].append(matrix[0+cnt])
    finalmat[i].append(matrix[1+cnt])
    finalmat[i].append(matrix[2+cnt])
    finalmat[i].append(matrix[3+cnt])
    cnt = cnt + 5

matches = []
for i in xrange(len(finalmat)):
    matches.append(0)

for i in xrange(len(finalmat)):
    prod = np.array(finalmat[i][0]) * np.array(finalmat[i][1]) * np.array(finalmat[i][2]) * np.array(finalmat[i][3])
    if 0 in prod:
        matches[i] = -1
    if 1 in prod:
        matches[i] = 'X won'
    if 3 in prod:
        matches[i] = 'X won'
    if 16 in prod:
        matches[i] = 'O won'
    if 24 in prod:
        matches[i] = 'O won'

for i in xrange(len(finalmat)):
    a = [finalmat[i][0][0], finalmat[i][1][0], finalmat[i][2][0], finalmat[i][3][0]]
    b = [finalmat[i][0][1], finalmat[i][1][1], finalmat[i][2][1], finalmat[i][3][1]]
    c = [finalmat[i][0][2], finalmat[i][1][2], finalmat[i][2][2], finalmat[i][3][2]]
    d = [finalmat[i][0][3], finalmat[i][1][3], finalmat[i][2][3], finalmat[i][3][3]]
    prod = np.array(a) * np.array(b) * np.array(c) * np.array(d)
    diag1prod = finalmat[i][0][0]*finalmat[i][1][1]*finalmat[i][2][2]*finalmat[i][3][3]
    diag2prod = finalmat[i][0][3]*finalmat[i][1][2]*finalmat[i][2][1]*finalmat[i][3][0]
    diagprod = [diag1prod, diag2prod]
    if 1 in prod or 1 in diagprod:
        matches[i] = 'X won'
    if 3 in prod or 3 in diagprod:
        matches[i] = 'X won'
    if 16 in prod or 16 in diagprod:
        matches[i] = 'O won'
    if 24 in prod or 24 in diagprod:
        matches[i] = 'O won'

f = open('out.dat', 'w')

for j in xrange(len(finalmat)):
  if matches[j] == 0:
      matches[j] = 'Draw'
  if matches[j] == -1:
      matches[j] = 'Game has not completed'
  f.write("Case #" + str(j+1) + ": " + str(matches[j]) + '\n')
f.close()
