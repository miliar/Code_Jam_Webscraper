import sys

def recycle(a, b):
    # convert the numbers to strings
    numStr = map(str, range(a, b+1))
    numDigits = len(numStr[0])
    numPoss = 0
    for n in numStr:
        for m in numStr:
            # compare works with strings
            if n >= m: continue
            for i in range(1, numDigits):
                if n[i:]+n[:i] == m:
                    numPoss += 1
                    break
    return numPoss

f = open('recyclenum-small.txt', 'w')
numTests = int(sys.stdin.readline())
lines = sys.stdin.readlines()
for i in range(1,numTests+1):
    line = lines[i-1].split()
    a = int(line[0])
    b = int(line[1])
    numPoss = recycle(a, b)
    f.write('Case #' + str(i) + ': ' + str(numPoss) + '\n')
f.close()
