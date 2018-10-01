from random import randint
from string import lowercase    

def process(lines):
    l,d,n = map(int,lines[0].split())
    words = lines[1:][:d]
    cases = lines[1+d:][:n]
    return process2(l,d,n,words,cases)
        

def caseToSets(case,l):
    sets=[None]*l
    setindex = 0
    i=0
    while i<len(case):
        if case[i]=='(':
            endi = case.find(')',i+1)
            sets[setindex] = set(case[i+1:endi])
            i=endi+1
        else:
            sets[setindex] = set(case[i])
            i+=1
        setindex+=1
    return sets

def process2_bak(l,d,n,words,cases):
    casesets = [caseToSets(x,l) for x in cases]
    validIndexChar = [ dict() for i in range(l)]
    for casei,caseset in enumerate(casesets):
        for i in range(l):
            for char in caseset[i]:
                validIndexChar[i].setdefault(char,set())
                validIndexChar[i][char].update([casei])

    for word in words:
        len(intersect([validIndexChar[i][d] for(i,d) in enumerate(word)]))
        
def process2(l,d,n,words,cases):
    return ['Case #%d: %d'%(casei+1,processCase(case,words,l)) for (casei,case) in enumerate(cases)]

def processCase(case,words,l):
    casesets = caseToSets(case,l)
    res=0
    for word in words:
        for chari,char in enumerate(word):
            if char not in casesets[chari]:
                break
        else:
            res+=1
    return res
        
