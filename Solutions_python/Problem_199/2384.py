import numpy as np
import sys
COUNTCASE = 1
if (len(sys.argv)==1):
    print('Required argument : sample file\n')
    exit()
result = open('result','w')
sample = open(sys.argv[1],'r')

nblines = sample.readline()
for k in range (int(nblines)):
    string = sample.readline()
    pancake = string.split()[0]
    maxflipper = int(string.split()[1])
    L = np.zeros(len(pancake))
    for k in range (len(pancake)):
        if pancake[k]=="+":
            L[k] = 1
        elif pancake[k]=="-":
            L[k] = -1
    index=0
    nbflip=0
    while (len(L[index:]) >= maxflipper):
        if L[index] == -1:
            L[index:index+maxflipper]*=-1
            nbflip+=1
        index += 1
    if (L == 1).all():
        result.write('Case #' + str(COUNTCASE) + ': '+ str(nbflip)+'\n')
    else:
        result.write('Case #' + str(COUNTCASE) + ': IMPOSSIBLE\n')
    COUNTCASE += 1

result.close()
sample.close()
