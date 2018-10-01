import os, sys
from math import *

def next_btn_for(who, sequence, start) :
    

    for i in range(start, len(sequence), 2):
        if sequence[i] == who:
            return int(sequence[i + 1])
    return -1
        

def min_time(nButtons, sequence):
    pos = {}
    pos['O'] = 1
    pos['B'] = 1
    time = 0
    for i in range(0, len(sequence), 2):
        who = sequence[i]
        btn = int(sequence[i + 1])
        other = None
        if who == 'B':
            other = 'O'
        else:
            other = 'B'
        moveToBtn = abs(pos[who] - btn)
        pos[who] = btn
        delta = moveToBtn + 1 #move time + press
        time += delta
        otherBtn = next_btn_for(other, sequence, i + 2)
        if otherBtn != -1:
            otherMove = abs(pos[other] - otherBtn)
            if delta >= otherMove:
                pos[other] = otherBtn
            else:
                if pos[other] > otherBtn:
                    pos[other] = pos[other] - delta
                else:
                    pos[other] = pos[other] + delta
    return time
        
            

nCases = int(sys.stdin.readline())

for case in range(1, nCases + 1):
    args = sys.stdin.readline().split()
    nButtons = int(args[0])
    print "Case #" + str(case) + ": " + str(min_time(nButtons, args[1:]))
