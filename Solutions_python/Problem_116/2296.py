#!/usr/bin/env python

import os
import sys

if len(sys.argv) < 2:
    sys.exit(0)
    
fin = open(sys.argv[1], "rb")
lines = fin.readlines()
fin.close()

numtest = int(lines[0])

#print "Test cases: %d" % numtest

ptr = 1
tests = []
for i in range(numtest):
    testlines = lines[ptr:ptr+4]
    tests.append(testlines)
    ptr += 5
    
#print tests

bingo_patterns = [
[0,1,2,3],
[4,5,6,7],
[8,9,10,11],
[12,13,14,15],

[0,4,8,12],
[1,5,9,13],
[2,6,10,14],
[3,7,11,15],

[0,5,10,15],
[3,6,9,12]
]

def CheckTestRecurse(test):
    #print "Recursing: %s" % test

    dotcount = test.count(".")
    if dotcount == 0:
        return CheckTest(test)
    else:
        winlist = []
        off = test.find(".")
        
        
        ntest = test[:off] + "O" + test[off+1:]
        ret = CheckTestRecurse(ntest)
        winlist.append(ret)
        
        ntest = test[:off] + "X" + test[off+1:]
        ret = CheckTestRecurse(ntest)
        winlist.append(ret)
        
        isT = test.find("T")
        if isT == -1:
            ntest = test[:off] + "T" + test[off+1:]
            ret = CheckTestRecurse(ntest)
            winlist.append(ret)
            
        #winlist

def CheckBingo(bingopans, tryme):
    #print bingopans
    #print tryme
    #print "--"*40
    for bingo in bingopans:
        bBroke = False
        #print bingo
        for elem in bingo:
            
            #print tryme
            #print "----------"
            #print "checking %s in %s" % (str(elem), "[" + ",".join(bingo) + "]")
            if elem in tryme:
                #print "its in"
                pass
            else:
                bBroke = True
                break
                
        if not bBroke:
            return True

def CheckTest(line):
    tspot = [i for i in range(len(line)) if line.startswith('T', i)]
    
    # check O win
    ospots = [i for i in range(len(line)) if line.startswith('O', i)]
    ospots += tspot
    if CheckBingo(bingo_patterns, ospots):
        #print ospots
        return "O won"
    
    xspots = [i for i in range(len(line)) if line.startswith('X', i)]
    xspots += tspot
    if CheckBingo(bingo_patterns, xspots):
        #print xspots
        return "X won"

    if "." in line:
        #print ospots
        #print line
        return "Game has not completed"

    #print xspots
    #print ospots
    return "Draw"
                    
                    
for i in range(len(tests)):

    oneliner = ""
    for l in tests[i]:
        oneliner += l.strip()
        
    ret = CheckTest(oneliner)
    #ret = CheckTest(tests[i])
    print "Case #%d: %s" % (i+1, ret)