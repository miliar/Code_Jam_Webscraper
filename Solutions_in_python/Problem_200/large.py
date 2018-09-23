import random
fw = open("output.out", "w")

def getCases():
    with open("B-large.in") as f:
        lines = f.read().splitlines() 
        T = int(lines[0])
        for t in range(1, T + 1):
            s = lines[t]
            yield {'t': t, 's': s}

def getMyCases():
    yield {'t': 1, 's': '442'}

def isTidy(n):
    previous = 10
    while n != 0:
        current = n % 10
        if current > previous:
            return False
        nStr = str(n)[0:len(str(n)) - 1] # n = n / 10 is not accurate
        if nStr == '':
            return True
        n = int(nStr)
        previous = current
    return True

def getTidyDelta(n):
    nStr = str(n)
    if len(nStr) == 1:
        return 0

    index = 1
    for i in range(1, len(nStr)):
        if int(nStr[i]) > int(nStr[i-1]):
            index = i + 1
        elif int(nStr[i]) < int(nStr[i-1]):
            return int(nStr[index:len(nStr)]) + 1
    return 0
        
    
for T in getCases():
    n = int(T['s'])
    delta = getTidyDelta(n)

    if not isTidy(n-delta):
        print ('Case #' + str(T['t']) + ': ' + str(n - delta))
    fw.write('Case #' + str(T['t']) + ': ' + str(n - delta) + '\n')


fw.close()
