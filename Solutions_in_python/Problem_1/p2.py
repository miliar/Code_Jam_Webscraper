#!/usr/bin/python

def isZero(E):
    for e in E:
        if E[e]== 0:
            return True
    return False
def setZero(E):
    for e in E:
        E[e]= 0
    return E
for case in range(input()):
    numE = int(raw_input())
    E = {}
    switches=0;
    for n in range(numE):
        E[raw_input()]=0
    numQ = int(raw_input())
    qs=[]
    for q in range(numQ):
        qu = raw_input()
        E[qu]+=1
        qs.append(qu)
        if isZero(E)== False:
            switches+=1
            E = setZero(E)
            E[qu]+=1
    print "Case #%i: %i" % (case+1,switches)
