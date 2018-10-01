'''
Created on Apr 12, 2013

@author: Phil
'''
def area(r):
    #area given inner radius
    return 2*r+1

fname = input('In file: ')
namefile = fname.split('.')[0]

import math

fr = open(fname, 'r')
fc = fr.read()
fr.close()

lines = fc.split('\n')
output = ""
numCases = int(lines[0])

for n in range(numCases):
    r = int(lines[n+1].split(' ')[0])
    t = int(lines[n+1].split(' ')[1])
    a = -2
    b = (1-2*r)
    root = int(math.floor((-b-math.sqrt(b*b-4*a*t))/2/a))
    output += "Case #"+str(n+1)+": "+str(root)+"\n"


output=output[:-1]
fw = open(namefile+'.out', 'w')
fw.write(output)
fw.close()