import sys

def calculateWP(m,x):
    total = 0
    wins = 0
    for char in m[x]:
        if char == '1':
            wins += 1
            total += 1
        elif char == '0':
            total += 1
    return float(wins)/total

def calculateOWP(m,x):
    total = 0
    wpOpp = 0
    for index in xrange(len(m[x])):
        if m[x][index] == '1' or m[x][index] == '0':
            tmpTotal = 0
            wins = 0
            for i in xrange(len(m[index])):
                if i == x:
                    continue
                elif m[index][i] == '1':
                    wins += 1
                    tmpTotal += 1
                elif m[index][i] == '0':
                    tmpTotal += 1
            wpOpp += float(wins)/tmpTotal
            total += 1
    return float(wpOpp)/total

def calculateOOWP(m,x):
    total = 0
    owpOpp = 0
    for index in xrange(len(m[x])):
        if m[x][index] == '1' or m[x][index] == '0':
            owpOpp += calculateOWP(m,index)
            total += 1
    return float(owpOpp)/total

f = open(sys.argv[1],'r')
t = int(f.readline())
for i in xrange(t):
    n = int(f.readline())
    m = []
    for x in xrange(n):
        tmp = []
        for char in f.readline()[:-1]:
           tmp.append(char)
        m.append(tmp)

    print "Case #%d:" % (i+1)
    for x in xrange(n):
        wp = calculateWP(m,x)
        owp = calculateOWP(m,x)
        oowp = calculateOOWP(m,x)
        answer = 0.25*wp + 0.50*owp + 0.25*oowp
        print answer
