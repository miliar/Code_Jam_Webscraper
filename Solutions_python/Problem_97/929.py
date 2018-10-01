#!/usr/bin/env python
import sys

fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')

lines = fin.readlines()
index = int(lines.pop(0))

for i in range(index):
    #read data
    numRange = lines.pop(0)
    num = numRange.rstrip().split(' ')
    
    count = 0
    lastadd = 0
    for a in range(int(num[0]), int(num[1])+1):
        number = str(a)
        
        for offest in range(len(number)):
            rnum = number[offest:] + number[:offest]

            if (a < int(rnum) and int(rnum) <= int(num[1]) and int(rnum) != int(lastadd)):
                count += 1
                lastadd = rnum
    
    #write result
    fout.write('Case #' + str(i+1) + ': ')
    fout.write(str(count) + '\n')
    
fout.close()