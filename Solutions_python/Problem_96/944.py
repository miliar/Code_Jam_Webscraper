#!/usr/bin/env python
import sys

fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')

lines = fin.readlines()
index = int(lines.pop(0))

for i in range(index):
    #read data
    numbers = lines.pop(0).rstrip().split(' ')
    t = int(numbers.pop(0))
    s = int(numbers.pop(0))
    p = int(numbers.pop(0))
    
    count = 0
    for j in range(t):
        if (int(numbers[j]) - p >= p*2 and p >= 0):
            count += 1
        elif (int(numbers[j]) - p >= (p-1)*2 and (p-1) >= 0):    #possible without surprise
            count += 1
        elif (int(numbers[j]) - p >= (p-2)*2 and (p-2) >= 0):    #possible with surprise
            if (s > 0):
                count += 1
                s -= 1
    
    #write result
    fout.write('Case #' + str(i+1) + ': ' + str(count))
    fout.write('\n')
    
fout.close()