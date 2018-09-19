#infile = open("test.txt")
infile = open("/Users/robertyaffe/Downloads/A-small-attempt1-1.in.txt")
outfile = open("codejamoutput.txt",'w')
import re
import math
from sets import Set
p = re.compile("-*\d+")
c = int(infile.readline())

for i in range(c):
    m = infile.readline()
    m = m.replace("\n","")
    x = Set()
    num = []
    for z in m:
        x.add(z)
        num.append(z)
    base = len(x)
    weird = False
    if base == 1:
        base = 2
        weird = True
    d = dict()
    d[m[0]] = 1
    done = False
    a = 1
    b = 0
    e = []
    e.append(0)
    for j in range(65):
        e.append(j+2)
    
    while not done:
        if weird:
            break
        if len(d.keys())==base:
            break
        if m[a] in d.keys():
            a = a + 1
        else:
            d[m[a]] = e[b]
            b = b + 1
            a = a + 1
        if len(d.keys())==base:
            done = True
    #print d
    ans = []
    for s in m:
        ans.append(d[s])
    #print ans
    answer = 0
    for t in range(len(ans)):
        answer  = answer + ans[len(ans)-t-1]*math.pow(base,t)
    
    
    outfile.write("Case #"+str((i+1))+": ")   
    outfile.write(str(int(answer)))
    outfile.write("\n")