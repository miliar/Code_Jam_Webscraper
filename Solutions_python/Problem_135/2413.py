#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
import sys

def solve(row1, deck1, row2, deck2):
    cand1 = set(deck1[row1 - 1])
    cand2 = set(deck2[row2 - 1])
    card = cand1.intersection(cand2)
    if len(card) == 0:
        return "Volunteer cheated!"
    elif len(card) == 1:
        return str(card.pop())
    else:
        return "Bad magician!"
    
    
# main
me = sys.argv[0].split("/")[-1].replace(".py", "")
#file = me + "-sample"
file = me + "-small-attempt0"
#file = me + "-large"

with open(file + ".in", "r") as fdin:
    with open(file + ".out", "w") as fdout:

        T = int(fdin.readline())
        for ncase in range(T):
            row1 = int(fdin.readline())
            deck1 = []
            for i in range(4):
                deck1.append([int(x) for x in fdin.readline().split()])

            row2 = int(fdin.readline())
            deck2 = []
            for i in range(4):
                deck2.append([int(x) for x in fdin.readline().split()])
            
            result = solve(row1, deck1, row2, deck2)
    
            line = "Case #%d: %s" % (ncase + 1, result)
            print(line) 
            fdout.write("%s\n" % line)
    