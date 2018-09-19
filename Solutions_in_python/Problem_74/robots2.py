#!/usr/bin/python

import sys

def seconds(lbo, lbb, order):
    secs = 0
    
    orange = 1
    blue = 1
    
    for o in order:
        cont = True
        while cont:
            if lbo:
                if orange != lbo[0]:
                    if orange > lbo[0]:
                        orange -= 1
                    else:
                        orange += 1
                else:
                    if o == 'O':
                        lbo = lbo[1:]
                        cont = False

            if lbb:
                if blue != lbb[0]:
                    if blue > lbb[0]:
                        blue -= 1
                    else:
                        blue += 1
                else:
                    if o == 'B':
                        lbb = lbb[1:]
                        cont = False
            secs += 1
    
    return secs


fd = open(sys.argv[1], 'r')
cases = int(fd.readline())

for c in range(0, cases):
    case = fd.readline().strip()
    case = case.split(' ')

    n = int(case[0])

    case = case[1:]

    lbo = []
    lbb = []
    order = []

    for i in range(0, n):
        o = case[i*2]
        if o == 'O':
            lbo.append(int(case[i*2+1]))
        else:
            lbb.append(int(case[i*2+1]))
        order.append(o)

    tmp = seconds(lbo, lbb, order)
    print "Case #%d: %d"%((c+1), tmp)
