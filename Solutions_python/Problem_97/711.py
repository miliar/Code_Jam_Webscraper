#!/usr/bin/python -tt


import sys
import random
import copy

def GetNext(num, mult):
    div = num / 10
    rem = num % 10

    if div == 0:
        return num
    return rem * mult + div
    

def GetRecycledCount(num, limit, mult, digcount):
    #print 'Check num = ', num
    temp = num
    cnt = 0
    pairs = set()
    for i in range(0, digcount):
        temp = GetNext(temp, mult)
        #print 'next = ', next
        if (temp > num) and (temp <= limit):
            if not (num, temp) in pairs:
                pairs.add((num, temp))
    return len(pairs)
    

def main():
    f = open('C-large.in')
    out = open('C-large.out','w')
    
    testcases = int(f.readline())
    print 'test number = ', testcases
    for tc in range(1, testcases + 1):
        print 'test case #', tc
        line = f.readline()
        #print 'line = ', line.split()
        val = [int(x) for x in line.split()]
        a = val[0]
        b = val[1]
        rc = 0;
        digcount = len(str(a)) - 1
        mult = 10**digcount
        print 'a = ', a, '  b = ', b
        #print 'digcoutn = ', digcount
        #print 'multiplier = ', mult
        pairs = []
        for i in range(a, b + 1):
            rc += GetRecycledCount(i, b, mult, digcount)
        print 'answer = ', rc
        #if (tc == 4):
        #    print 'pairs', pairs

        #for i in range(0, len(pairs)):
        #    for j in range(i + 1, len(pairs)):
        #        if (pairs[i][0] == pairs[j][0]) and (pairs[i][1] == pairs[j][1]):
        #            print 'equal pairs found ', pairs[i], pairs[j], ' i = ', i, ' , j = ', j
                    
        
        out.write('Case #'+str(tc)+': '+str(rc)+'\n')
            
    f.close()
    out.close()   
    


if __name__ == '__main__':
  main()
