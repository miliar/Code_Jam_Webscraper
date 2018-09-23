def getTimes(fd,L):
    tl = []
    for i in range(0,len(L)):
        h = L[i]
        r = fd - h[0]
        s = h[1]
        t = r/s
        tl.append(t)
    return tl

def findMax(timeList):
    t = timeList[0]
    mt = t
    h = 0
    for i in range(0,len(timeList)):
        t = timeList[i]
        if t > mt :
            h = i
    return h


def findLow(L):
    t = L[0]
    sl = t[1]
    h=0
    for i in range(0,len(L)):
        t = L[i]
        s = t[1]
        if s < sl:
            h = i

    return h

def calcSpeed(t,hl):
    fd = t
    sh = findMax(getTimes(fd,hl))
    h = hl[sh]
    d = h[0]
    s = h[1]
    lspeed = float(fd / ((fd-d)/s))
    return '%.6f'%(lspeed)

# read input N
file = open("A-small-attempt5.in", "r")
Testcases = int(file.readline())
#print Testcases

outfile = open("A-small-attempt5.out","w")

for x in range(1, Testcases+1):
    val = file.readline()
    NewVal = val.split(' ')
    fd= float(NewVal[0])
    n = int(NewVal[1])
    l = []
    for y in range(0,n):
        r = file.readline()
        hval = r.split(' ')
        d = float(hval[0])
        s = float(hval[1])
        l.append([d,s])

    result = calcSpeed(fd,l)

    #print result
    OutputText = "Case #" + str(x) + ": " + str(result)
    outfile.write(OutputText + '\n')

file.close()
outfile.close()