#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

#input_lines = """
#
#Input
#
#3
#4 O 2 B 1 B 2 O 4
#3 O 5 O 8 B 100
#2 B 2 B 1""".split('\n')

input_lines = sys.stdin.readlines();

if __name__ == '__main__':
    problem_lines = input_lines[1:]

    totalTime = []
    for line in problem_lines:
        tmp = line.split(' ')[1:]
        seq =  zip( tmp[0::2], tmp[1::2] )

        currentOrangeTime = 0
        currentOrangePos = 1
        currentBlueTime = 0
        currentBluePos = 1
        for com in seq:
            robotColor = com[0]
            buttonNumber = int( com[1] )

            if robotColor == 'O':
                movVect = buttonNumber - currentOrangePos
                addTime = abs( movVect ) + 1

                currentOrangeTime += addTime
                currentOrangePos += movVect

                if currentOrangeTime <= currentBlueTime:
                    currentOrangeTime = currentBlueTime + 1
            elif robotColor == 'B':
                movVect = buttonNumber - currentBluePos
                addTime = abs( movVect ) + 1

                currentBlueTime += addTime
                currentBluePos += movVect

                if currentBlueTime <= currentOrangeTime:
                    currentBlueTime = currentOrangeTime + 1

        totalTime.append( max( currentOrangeTime, currentBlueTime ) )

    for n, result in zip( range(1, len( totalTime ) + 1 ), totalTime ):
        print "Case #%d: %d" % ( n, result )
