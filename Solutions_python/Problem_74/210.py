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

    str1 = lines[z+1].split(' ', 1)
    num = int(str1[0])
    seq = [ [0,0] for b in range(num)]
    vals = str1[1].split(' ')
    for a in range(num):
        seq[a][0] = vals[2*a]
        seq[a][1] = int(vals[2*a+1])
       
       
    oPos = 1
    bPos = 1 
    time = 0
    for a in range(num):
        cstep = seq[a]
        if cstep[0]=='B' :
           if bPos==cstep[1]:
               time = time+1
               for c in range(num-a-1):
                   if seq[a+c+1][0]=='O':
                       if not oPos==seq[a+c+1][1]:
                           oPos = oPos -((oPos-seq[a+c+1][1])/abs(oPos-seq[a+c+1][1]))
                       break
           else :
               time = time + abs(bPos - cstep[1]) + 1
               for c in range(num-a-1):
                   if seq[a+c+1][0]=='O':
                       if not oPos==seq[a+c+1][1]:
                           oPos = oPos -((oPos-seq[a+c+1][1])/abs(oPos-seq[a+c+1][1]))*min([abs(bPos-cstep[1])+1, abs(oPos-seq[a+c+1][1])])
                       break
               bPos = cstep[1]
        else :
            if oPos==cstep[1]:
               time = time+1
               for c in range(num-a-1):
                   if seq[a+c+1][0]=='B':
                       if not bPos==seq[a+c+1][1]:
                           bPos = bPos -((bPos-seq[a+c+1][1])/abs(bPos-seq[a+c+1][1]))
                       break
            else :
                time = time + abs(oPos - cstep[1]) + 1
                for c in range(num-a-1):
                   if seq[a+c+1][0]=='B':
                       if not bPos==seq[a+c+1][1]:
                           bPos = bPos -((bPos-seq[a+c+1][1])/abs(bPos-seq[a+c+1][1]))*min([abs(oPos-cstep[1])+1, abs(bPos-seq[a+c+1][1])])
                       break
                oPos = cstep[1]
    output = output + "Case #"+str(z+1)+": "+str(time)+"\n"

output=output[:-1]
fw = open(namefile+'.txt', 'w')
fw.write(output)
fw.close()