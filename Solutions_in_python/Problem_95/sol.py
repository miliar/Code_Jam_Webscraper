import qp1
import sys

inputfile = open(sys.argv[1],'r').read()
incase = inputfile.split('\n')
del incase[0], incase[-1]
translate = qp1.translate
translate['z'] = 'q'
translate['q'] = 'z'
l = [list(i) for i in incase]

for i in range(len(l)):
  for j in range(len(l[i])):
    l[i][j] = translate[l[i][j]]

l = [''.join(i) for i in l]

caseCount = 0
for sen in l:
  caseCount+=1
  print 'Case #'+str(caseCount)+': '+sen
