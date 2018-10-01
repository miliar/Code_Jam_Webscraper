#!/usr/bin/env python2

import sys

def gcj(f):
    with open(f, 'r') as datafile:
        t = int(datafile.readline())
        data = datafile.read()
        for c,dataset in enumerate(data.split("\n\n")):
            if dataset:
                print 'Case #{}: {}'.format(c+1, process(dataset))

def process(dataset):
    mapelem = {'X':1, 'O':-1, 'T':0}
    row = [0]*4
    col = [0]*4
    diag = [0]*2
    for i,line in enumerate(dataset.split()):
        for j,elem in enumerate(line):
            if elem == '.':
                row[i] = None
                col[j] = None
                if i == j:
                    diag[0] = None
                if i + j == 3:
                    diag[1] = None
                continue
            x = mapelem[elem]
            if row[i] != None: row[i] += x
            if col[j] != None: col[j] += x
            if i == j:
                if diag[0] != None: diag[0] += x
            if i+j == 3:
                if diag[1] != None: diag[1] += x
    score = row+col+diag
    if 3 in score or 4 in score:
        return 'X won'
    elif -3 in score or -4 in score:
        return 'O won'
    elif None in score:
        return 'Game has not completed'
    else:
        return 'Draw'



gcj(sys.argv[1])
