#!/usr/bin/python
from __builtin__ import list


import sys, os, time,  string

'''
  Code jam 2014 - huls
'''

INPUT_FILE = "c:\\cj2014\\B-small-attempt1.in"
OUTPUT_FILE = "c:\\cj2014\\B-small-attempt1.out"
'''
INPUT_FILE = "c:\\cj2014\\B.in"
OUTPUT_FILE = "c:\\cj2014\\B.out"
'''
f_in = open(INPUT_FILE, 'r')
f_out = open(OUTPUT_FILE, 'w')



def solve():
    myXY = f_in.readline().split()
    C = float(myXY[0])
    F = float(myXY[1])
    X = float(myXY[2])

    currentCookieSpeed = 2
    collapsedTime = 0.0
    isDone = False
    timeList = list()
    prevMin = 100000000000000000.0
    prevmincounter = 0;
    while ( not isDone) :
        tmpVar = collapsedTime + X/currentCookieSpeed
        timeList.append(tmpVar)
        collapsedTime = collapsedTime + ( C / currentCookieSpeed )
        currentCookieSpeed = currentCookieSpeed + F
        if ( min(timeList) >= prevMin):
            if (prevmincounter == 4):
                return prevMin 
            prevmincounter = prevmincounter + 1
        else:
            prevMin = min(timeList)
        
    '''sorted(timeList, key=float, reverse=True) 
    return timeList.pop()'''

def main():
    T = int(f_in.readline())
    for case in range(1, T+1):
        print case
        sol = solve()
        f_out.write("Case #" + str(case) + ": " + ("%.7f" % sol) + "\n")
    print "Finished"
    
if __name__ == "__main__":
    startTime = time.clock()
    main()
    print "Completed in {} seconds. \n" . format(time.clock() - startTime)