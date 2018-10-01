__author__ = 'udi'
import sys

def calcTime(F,C,X,a):
    sum = 0
    for i in range(0,a):
        time = C/(2+i*F)
        sum+=time
    sum+=X/(2+a*F)
    return sum

f = open(sys.argv[1])
T = int(f.readline())
for j in range(1,T+1):
    line = f.readline()
    line = line.split()
    C = float(line[0])
    F = float(line[1])
    X = float(line[2])
    a=0
    result = calcTime(F,C,X,a)
    a+=1
    notEnded = True
    while(notEnded):
        newResult = calcTime(F,C,X,a)
        if (newResult>result):
            notEnded=False
            break
        result = newResult
        a+=1
    print "Case #"+str(j)+": %.7f"% result



