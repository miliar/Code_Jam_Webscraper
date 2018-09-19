##Google Code Jam 2015
#Input File
file = open('D-small-attempt3.in','r')       
#Output File
output = open('output.out','w')

#Imports
import math

#Functions
def val(line):
    vals = []
    l = ''
    for i in line:
        if i == ' ':
            vals.append(int(l))
            l = ''
        else:
            l += i
    vals.append(int(l))
    return vals

#test cases
t = int(file.readline())
for i in range(0,t):
    res = ""
    x, r, c = val(file.readline().strip('\n'))
##    if r*c % x != 0 or (x>2 and r*c==x) or int((x+1)/2)> min(r,c):
##        res = "RICHARD"   
##    else:
##        res = "GABRIEL"
    if x==1:
        res = "GABRIEL"
    if x==2:
        if r*c%2==0:
            res = "GABRIEL"
        else:
            res = "RICHARD"
    if x==3:
        if r*c%3==0 and (r*c/3)>=2:
            res = "GABRIEL"
        else:
            res = "RICHARD"
    if x==4:
        if r*c%4==0 and (r*c/4)>=3:
            res = "GABRIEL"
        else:
            res = "RICHARD"
    c = i +1
    output.write('Case #%i:'%c +' '+res +'\n')

output.close()
file.close()
