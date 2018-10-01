"""
Created by bob on 11/04/15
"""

import logging


def set_up_logging(level='info'):
    level = getattr(logging, level.upper())
    logging.basicConfig(filename='qualification.log', level=level,
                        format='%(asctime)s %(levelname)s:%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

with open('D-small-attempt0.in') as f:
    testcases = int(f.readline().strip())
    print 'test cases', testcases
    outlist=[]
    for i in range(testcases):
        test = f.readline().strip().split()
        x,r,c = test
        x = int(x)
        r = int(r)
        c = int(c)
        print i+1, x, r,c
        if x == 1:
            win = 'GABRIEL'
        if x == 2:
            if (r*c)%2 == 0:
                win =  'GABRIEL'
            else:
                win =  'RICHARD'
        if x==3:
            if min((r,c)) == 1:
               win =  'RICHARD'
            elif (r*c)%3 == 0:
                win =  'GABRIEL'
            else:
               win =  'RICHARD'
        if x==4:
            if min((r,c)) in (1,2):
               win =  'RICHARD'
            elif (r*c)%4 == 0:
                win =  'GABRIEL'
            else:
                win =  'RICHARD'
        outlist.append((str(i+1),win))
with open('block.out', 'w') as f:
    for test, result in outlist:
        f.write('Case #' + test + ': ' + result + '\n')


