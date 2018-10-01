import sys
from math import log

def isEven(n):
    return n % 2 == 0


inputFilepath = sys.argv[1]
output = []

with open(inputFilepath, 'r') as f:
    lines = f.readlines()

    for i in range(1,len(lines)):
        line = lines[i].strip()

        n, k = line.split(' ')

        n = int(n)
        k = int(k)
        
        generation = int(log(k, 2))
        area = int(((n - k) / (2 ** generation)) + 1)

        l = r = 0

        if isEven(area):
            l = (area / 2) - 1
            r = (area / 2)
        else:
            l = r = int(area / 2)

        output.append('Case #%d: %d %d' % (i, max(l,r), min(l,r)))

with open('output.txt', 'w') as f:
    f.write('\n'.join(output))



