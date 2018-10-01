#!/bin/python

def transformRows(ncols, letterPosns):
    result = []
    firstNonEmptyRow = -1
    lastRow = None
    for i, rowEnc in enumerate(letterPosns):
        row = []
        last = None
        for (col, c, length) in rowEnc:
            row.extend([c] * (length+1))
            last = c
        if last != None:
            row.extend([last] * (ncols - len(row)))
        if row == []:
            if lastRow != None:
                row = lastRow
        else:
            if firstNonEmptyRow < 0:
                firstNonEmptyRow = i
            lastRow = row
        result.append(row)
    # still need to process first row if empty
    row = result[firstNonEmptyRow]
    for i in xrange(firstNonEmptyRow):
        result[i] = row
    return result

def findLetters(cake):
    result = []
    for (i, row) in enumerate(cake):
        count = 0
        rrow = []
        for j, c in enumerate(row):
            if c != '?':
                rrow.append((j, c, count))
                count = 0
            else:
                count += 1
        result.append(rrow)
    return result

t = int(raw_input().strip())
for test in xrange(1, t+1):
    r, c = map(int, raw_input().strip().split(' '))
    cake = []
    for i in xrange(r):
        row = raw_input().strip()
        cake.append(row)
    posns = findLetters(cake)
    labeledCake = transformRows(c, posns)
    print "Case #%d:" % test
    for row in labeledCake:
        print "".join(row)
    
