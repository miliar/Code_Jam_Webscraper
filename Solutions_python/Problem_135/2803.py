'''
Created on Apr 12, 2014

@author: Yuan
'''

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        first = int(raw_input())
        firstmap = []
        for j in range(4):
            firstmap.append([int(x) for x in raw_input().split(' ')])
        second = int(raw_input())
        secondmap = []
        for j in range(4):
            secondmap.append([int(x) for x in raw_input().split(' ')])
        match = [x for x in firstmap[first-1] if x in secondmap[second-1]]
        print "Case #%d: " % (i+1),
        if len(match)==0:
            print "Volunteer cheated!"
        elif len(match)==1:
            print match[0]
        else:
            print "Bad magician!"        
    