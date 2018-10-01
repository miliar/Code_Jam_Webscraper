#!/usr/bin/env python
# -*- coding: utf-8 -*-


src = u"A-small-attempt1.in"
dst = "A-small.out"

def process(src, dst):
    
    fo = open(dst, 'w')
    itr = 0
    #Dict = {}
    first = 0
    second = 0
    firstRow = []
    secondRow = []
    caseItr = 1
    
    for line in open(src):
        line = line.strip()
        
        
        if itr == 0:
            T = int(line)
        elif itr%10 == 1:
            first = int(line)
        elif itr%10 == 2:
            row = line.split(' ')
            row2 = []
            for i in row:
                row2.append(int(i))
            firstRow.append(row2)
        elif itr%10 == 3:
            row = line.split(' ')
            row2 = []
            for i in row:
                row2.append(int(i))
            firstRow.append(row2)
        elif itr%10 == 4:
            row = line.split(' ')
            row2 = []
            for i in row:
                row2.append(int(i))
            firstRow.append(row2)
        elif itr%10 == 5:
            row = line.split(' ')
            row2 = []
            for i in row:
                row2.append(int(i))
            firstRow.append(row2)
        elif itr%10 == 6:
            second = int(line)
        elif itr%10 == 7:
            row = line.split(' ')
            row2 = []
            for i in row:
                row2.append(int(i))
            secondRow.append(row2)
        elif itr%10 == 8:
            row = line.split(' ')
            row2 = []
            for i in row:
                row2.append(int(i))
            secondRow.append(row2)
        elif itr%10 == 9:
            row = line.split(' ')
            row2 = []
            for i in row:
                row2.append(int(i))
            secondRow.append(row2)
        elif itr%10 == 0 and itr > 0:
            row = line.split(' ')
            row2 = []
            for i in row:
                row2.append(int(i))
            secondRow.append(row2)
            
            #print first, second, firstRow, secondRow
            #print firstRow[(first-1)]
            #print secondRow[(second-1)]
            
            firstSet = set(firstRow[(first-1)])
            secondSet = set(secondRow[(second-1)])
            result = firstSet.intersection(secondSet)
            #print result, len(result), list(result)
            
            if len(result) == 1:
                answer = "Case #" + str(caseItr) + ": " + str(list(result)[0])
                print answer
                #print "Case #", caseItr, " ",  list(result)[0]
            if len(result) == 0:
                answer = "Case #" + str(caseItr) + ": " + "Volunteer cheated!"
                print answer
                #print "Case #", caseItr, " ",  "Bad magician!"
            if len(result) > 1:
                answer = "Case #" + str(caseItr) + ": " + "Bad magician!"
                print answer
                #print "Case #", caseItr, " ",  "Volunteer cheated!"
            fo.write(answer + "\n")
            #初期化
            first = 0
            second = 0
            firstRow = []
            secondRow = []
            caseItr += 1
            #itr += 1
        
        #print itr%10
        itr += 1
        
if __name__ == '__main__':
    
    process(src, dst)
    