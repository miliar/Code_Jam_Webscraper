def getToken(filename):
    inputFile = open(filename, 'r')
    for line in inputFile:
        tokens = line.split()
        for token in tokens:
            if token != '':
                yield token
    inputFile.close()

inputFilename = 'A-large.in'
outputFilename = 'A-large.txt'

tokenIterator = getToken(inputFilename)
def get():return tokenIterator.next()
def getint(): return int(get())
outputFile = open(outputFilename, 'w')

# END PRE-PROCESSING

caseNum = getint()
for case in range(caseNum):

    x = getint()
    s = getint()
    r = getint()
    runt = getint()
    n = getint()
    time = 0.0
    pos = 0.0
    ww = []
    laste = 0
    for i in range(n):
        b = getint()
        e = getint()
        w = getint()
        ww.append((0,laste,b))
        ww.append((w,b,e))
        laste = e
    ww.append((0,laste,x))
    ww.sort()
    for i in range(len(ww)):
        w,b,e = ww[i]
        dist = e-b
        speed = w
        if runt > float(dist)/(speed+r):
            time += float(dist)/(speed+r)
            runt -= float(dist)/(speed+r)
        else:
            walkt = (float(dist) - (speed+r)*runt)/(speed+s)
            time += walkt + runt
            runt = 0
        
    output = "Case #"+str(case+1)+": "+str(time)+"\n"
    outputFile.write(output)

# BEGIN POST-PROCESSING
outputFile.close()

