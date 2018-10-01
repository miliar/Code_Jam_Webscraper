def parse(inp):
    op = []
    for letter in inp:
        if letter == '+':
            op.append(1)
        else:
            op.append(-1)
    return op

#test = parse("+++---+")
#print test

def unparse(inp):
    op = ""
    for i in inp:
        if i==-1:
            op+="-"
        else:
            op+="+"
    return op

#print unparse(test)

def flip(cur, ind, num):
    i = ind
    t = cur[:]
    while i< ind+num:
        t[i]*=-1
        i+=1
    return t

def solve(line):
    l = line.split(" ")
    s = parse(l[0])
    k = int(l[1])
    i = 0
    flips = 0
    while i<len(s)-k+1:
        if s[i] == -1:
            s = flip(s,i,k)
            flips+=1
            i+=1
        else:
            i+=1
    
    while i<len(s):
        if s[i] == -1:
            flips = -1
            break
        i+=1
    
    if flips == -1:
        return "IMPOSSIBLE"
    else:
        return str(flips)

import sys
filename = sys.argv[1]
f = open(filename, "r")
s = f.read()
f.close()
lines = s.split("\n")
lines = [l.strip() for l in lines]
T = int(lines[0])
for i in range(T+1):
    if i==0:
        continue
    line = lines[i]
    ans = solve(line)
    print "Case #"+str(i)+": "+ans