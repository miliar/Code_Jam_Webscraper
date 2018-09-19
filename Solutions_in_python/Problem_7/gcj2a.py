import re
import string

f = open('C:\\Users\\Moose\\workspace\\gcj2A\\A-small-attempt0.in','r')
#f = open('C:\\Users\\Moose\\workspace\\gcj2A\\A-large.in','r')

class Tree:
    x = 0
    y = 0
    def __init__(self,tx,ty):
        self.x = tx
        self.y = ty

nbCases = int(f.readline())
for caseNb in range(0,nbCases):
    arInput = []
    arInput = re.split(' ' ,string.strip(f.readline()))
    n = int(arInput[0])
    A = int(arInput[1])
    B = int(arInput[2])
    C = int(arInput[3])
    D = int(arInput[4])
    x0 = int(arInput[5])
    y0 = int(arInput[6])
    M = int(arInput[7])
    arTrees = []
    tree = Tree(x0,y0)
    arTrees.append(tree)
    x = x0
    y = y0
    for i in range(1,n):
        x = (A * x + B) % M
        y = (C * y + D) % M
        tree = Tree(x,y)
        arTrees.append(tree)
        #print "Tree " + str(i) + ":" + str(arTrees[i].x) + " " + str(arTrees[i].y)
    nbTri = 0
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (( (arTrees[i].x + arTrees[j].x + arTrees[k].x) % 3 == 0 ) and ((arTrees[i].y + arTrees[j].y + arTrees[k].y) % 3 == 0)):
                    nbTri += 1
    print "Case #" + str(caseNb+1)+": " + str(nbTri)
    
    


f.close()