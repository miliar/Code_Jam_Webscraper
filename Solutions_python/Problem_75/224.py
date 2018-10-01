'''
Created on May 6, 2011

Google Code Jam

user: philipbo

@author: Phil Bozak
'''

import os
thisname = os.path.basename(__file__)
namefile = thisname.split('.')[0]

fr = open(namefile+'.in', 'r')
fc = fr.read()
fr.close()

lines = fc.split('\n')
numCases = int(lines[0])

output = ""

for z in range(numCases):
    strin = lines[z+1]
    items = strin.split(' ')
    numComb = int(items[0])
    strComb = items[1:numComb+1]
    numOpp = int(items[numComb+1])
    strOpp = items[numComb+2:numComb+numOpp+2]
    strTest = items[-1]
    
    combs = [ 0 for a in range(numComb)]
    for a in range(numComb):
        combs[a] = [strComb[a][0], strComb[a][1], strComb[a][2]]
        
    opps = [0 for a in range(numOpp)]
    for a in range(numOpp):
        opps[a] = [strOpp[a][0], strOpp[a][1]]
    
    outStr = strTest[0]
    b=1
    while b<(len(strTest)):
        combo = False
        if len(outStr)>0:
            for comb in combs:
                if (comb[0]==strTest[b] and comb[1]==outStr[-1]) or (comb[1]==strTest[b] and comb[0]==outStr[-1]):
                    outStr = outStr[:-1]+comb[2]
                    combo = True
                    break
        
        if not combo:
            outStr = outStr + strTest[b]
            for opp in opps:
                if strTest[b]==opp[0]:
                    start = outStr.find(opp[1])
                    if not (start==-1):
                        outStr = ""
                if strTest[b]==opp[1]:
                    start = outStr.find(opp[0])
                    if not (start==-1):
                        outStr = ""
        b=b+1
    
    ans = "["
    for d in outStr:
        ans = ans + d + ", "
    if len(outStr)>0:
        ans = ans[:-2]
    ans = ans+"]"
    
    output = output + "Case #"+str(z+1)+": "+ans+"\n"

output = output[:-1]

fw = open(namefile+'.txt', 'w')
fw.write(output)
fw.close()