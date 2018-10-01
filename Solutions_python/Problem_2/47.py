#!/usr/bin/env python

from sys import *

def timeDecode(time):
    h = time / 60
    m = int (time / time / 60)
    return "%02d:%02d" % (h, m)

def processCase(trainsA, trainsB, tt, case):
    if len(trainsA) == 0 or len(trainsB) == 0:
        ca = len(trainsA)
        cb = len(trainsB)
        
    else:        
        ca = 0
        cb = 0
        
        dictA = {}        
        trainsA.sort()
        trainsB.sort(lambda a,b: cmp(b[1], a[1]))
        
        for i in range(0, len(trainsA)):
            found = False
            
            for j in range(0, len(trainsB)):
                if trainsA[i][0] >= trainsB[j][1] + tt and not dictA.has_key(j):
                    dictA[j] = True
                    found = True
                    break
                    
            if not found: ca += 1
        
        dictB = {}      
        trainsA.sort(lambda a,b: cmp(b[1], a[1]))
        trainsB.sort()
                    
        for i in range(0, len(trainsB)):
            found = False
            
            for j in range(0, len(trainsA)):
                if trainsB[i][0] >= trainsA[j][1] + tt and not dictB.has_key(j):
                    dictB[j] = True
                    found = True
                    break
                    
            if not found: cb += 1
        
    print "Case #%d: %d %d" % (case, ca, cb)    
    return

def timeEncode(time):
    (h, m) = time.split(':')
    return int (h) * 60 + int (m)

def process(lines):
    n = int (lines[0])
    case = 1
    i = 1
    while case <= n:
        tt = int (lines[i].strip("\r\n"))
        (a, b) = lines[i + 1].strip("\r\n").split(' ')
        (ac, bc) = int(a), int(b)
        i += 2
        
        trainsA = []
        trainsB = []
        while ac > 0:
            (dep, arr) = lines[i].strip("\r\n").split(' ')
            trainsA.append((timeEncode(dep), timeEncode(arr)))
            i += 1
            ac -= 1
        
        while bc > 0:
            (dep, arr) = lines[i].strip("\r\n").split(' ')
            trainsB.append((timeEncode(dep), timeEncode(arr)))
            i += 1
            bc -= 1
            
        processCase(trainsA, trainsB, tt, case)
        case += 1
        

def usage():
    print "Usage %s input" % argv[0]

def main():    
    if len(argv) < 2:
        usage()
        exit()
        
    input = argv[1]
    f = open(input, 'r')
    
    try:
        lines = f.readlines()
        process(lines)
        
    finally:
        f.close()

if __name__ == '__main__':
    main()
    