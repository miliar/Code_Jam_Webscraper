#! /usr/bin/python
import sys
import string

cases = int(sys.stdin.readline()[:-1])
actual_case = 0

while actual_case < cases:
    # reading and so
    actual_case += 1
    
    numbers = sys.stdin.readline()[:-1].split()
    r = int(numbers[0])
    c = int(numbers[1])

    pict = []
    #nacitani cisel v radku do promenne
    for i in range(r):
        line = sys.stdin.readline()[:-1]
        line_list = [i for i in line]
        pict.append(line_list)

    possible = True

    for j in range(r):
        for i in range(c):
            if pict[j][i] == '#':
                pict[j][i] = '/'
                if ((i+1 < c) and (pict[j][i+1] == '#')):
                    pict[j][i+1] = '\\'
                else:
                    possible = False
                if ((j+1 < r) and (pict[j+1][i] == '#')):
                    pict[j+1][i] = '\\'
                else:
                    possible = False
                if ((i+1 < c) and (j+1 < r) and (pict[j+1][i+1] == '#')):
                    pict[j+1][i+1] = '/'
                else:
                    possible = False

    pict_new = []
    for row in pict:
        pict_new.append(''.join(row))

    print "Case #%d:" %(actual_case)
    if possible:
        for row in pict_new:
            print row
    else:
        print "Impossible"


