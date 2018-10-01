#Google Code Jam 2012
#Problem C
#Andrew Penland
#April 13, 2012

import shlex

def Cycle(m,i):
    return m[len(m)-i:] + m[0:len(m)-i]

def RecycledNumbers(m,n):
    total = 0
    for i in range(m,n+1):
        cycles = []
        x = str(i)
        for j in range(len(x)):
            new_x = int(Cycle(x,j))
            if new_x > i and not (new_x > n) and not(new_x in cycles):
                cycles.append(new_x)
        total = total + len(cycles)
    return total

f1 = open('C:/C-small-attempt0.in','r')
f2 = open('C:/Problem3Solution.txt','w')

numlines = int(f1.readline())
lines = f1.readlines()

for i in range(numlines):
    line = lines[i].rstrip()
    line = shlex.split(line)
    a = int(line[0])
    b = int(line[1])
    f2.write("Case #" + str(i + 1) + ": " + str(RecycledNumbers(a,b)) + "\n")

f2.close()
f1.close()

    
