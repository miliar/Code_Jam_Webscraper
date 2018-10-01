'''
Created on Apr 13, 2013

@author: Kyle
'''
import math
import sys

def perfect_squares(low, high):
    lowest = int(math.ceil(math.sqrt(low)))
    highest = int(math.sqrt(high))
    return (n**2 for n in range(lowest, highest + 1))

def readFile():
    
    with open('input.in') as f:
        intArray = []
        for line in f:
            line = line.split()
            if line:
                for i in line:
                    intArray.append(int(i))
    
        return intArray
    ''''f = open('input.in', 'r')
    return list(map(int, f.read().strip().split('\n')))'''

def main():
    fileLines = readFile()
    cases = fileLines[0]
    index = 1

    for case in xrange(1, cases + 1):
        counter = 0
        low = fileLines[index]
        index += 1
        high = fileLines[index]
        index += 1
        for ps in perfect_squares(low, high):
            if str(ps) == str(ps)[::-1]:
                sps = int(math.sqrt(ps))
                if(str(sps) == str(sps)[::-1]):
                    counter +=1
        print "Case #{0}: {1}".format(case, counter)
        
        
if __name__ == '__main__':
    main()
        
        