import sys
import re

ST = "welcome to code jam"
def calc(line,place):
##    print line,place
    if not line:
        if place==len(ST):
            return 1
        else:
            return 0
    if place==len(ST):
        return 1
    
    if line[0]==ST[place]:
        return calc(line[1:],place+1)+calc(line[1:],place)
    else:
        return calc(line[1:],place)

#filename = "C:\\Amir\\programming\\CodeJam\\first\\3\\in-small.txt"
    
filename = "C:\\Amir\\programming\\CodeJam\\first\\3\\C-small.in"
f = open(filename)
lines = f.readlines()
f.close()
lines.reverse()
firstLine = lines.pop()
#print firstLine
times = int(firstLine)
out = open("C:\\Amir\\programming\\CodeJam\\first\\3\\out.txt",'w')
for z in range(times):
    line = lines.pop()
##    print line
    result = calc(line,0)
    result = result%10000
    output = str(result)
    # ugly, but quick (can use also the printf formatation...)
    if (result < 10):
        output = "000"+output
    elif (result < 100):
        output = "00"+output
    elif (result < 1000):
        output = "0"+output
    out.write("Case #"+str(z+1)+": "+output+"\n")
out.close()
