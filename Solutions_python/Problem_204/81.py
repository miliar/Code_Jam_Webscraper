'''
Created on Apr 14, 2017

@author: Jarred
'''
from sys import stdin as cin

data=cin.readline

cases=int(data())

def can_remove(packages, mins, maxs):
    for i in range(len(packages)):
        index=0
        while index<len(packages[i]) and packages[i][index]<mins[i]:
            index+=1
        if index>=len(packages[i]) or packages[i][index]>maxs[i]:
            return False
    return True


def getIndex(package, minVal):
    if package.count(minVal)>0:
        return package.index(minVal)
    else:
        index=0
        while package[index]<minVal:
            index+=1
        return index

for case in range(1,1+cases):
    line=data().split()
    n=int(line[0])
    p=int(line[1])
    
    amts=data().split()
    for i in range(len(amts)):
        amts[i]=int(amts[i])
    
    packages=[data().split() for i in range(n)]
    for a in range(len(packages)):
        for b in range(len(packages[a])):
            packages[a][b]=int(packages[a][b])
        packages[a].sort()
    
    num=0
    servings=1
    while(len(packages[a])>0 and servings*amts[0]*.9<=packages[0][-1]):
        ideal=[servings*amts[a] for a in range(len(amts))]
        mins=[.9*ideal[a] for a in range(len(ideal))]
        maxs=[1.1*ideal[a] for a in range(len(ideal))]
        while can_remove(packages, mins, maxs):
            indices=[getIndex(packages[a], mins[a]) for a in range(len(packages))]
            num+=1
            #print(indices, packages, sep='\n')
            packages=[packages[a][:indices[a]]+packages[a][indices[a]+1:] for a in range(len(indices))]
        servings+=1
    
    print('Case #'+str(case)+':', num)
    #print(packages)