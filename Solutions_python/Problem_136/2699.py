__author__ = 'MERT'

def findMinTime(C,F,X,currentRate):
    if C >= X:
        return X/currentRate
    else:
        results = [X/currentRate]
        fcount = 1
        fgrab = 0
        while True:
            results.append(fgrab + C/currentRate + X/(currentRate + F))
            fcount += 1
            if results[fcount-2] < results[fcount-1]:
                break
            fgrab += C/currentRate
            currentRate += F
        return results[fcount-2]

inp = open("B-large.in","r")
output = open("output2.txt","w")
line = inp.readline()
numberOfTest = int(line)
for case in range(1,numberOfTest+1):
    line = inp.readline().split(' ')
    C = float(line[0])
    F = float(line[1])
    X = float(line[2])
    result = findMinTime(C,F,X,2.0)
    output.writelines("Case #" + str(case) + ": " + str(result) + "\n")
output.close()

