#!/bin/python
import sys
import copy

def readFile(fname):
    with open(fname) as f:
            contents = f.read().splitlines()
    ncases = int(contents.pop(0))
    nlines = len(contents)/ncases
    cases = [[] for x in range(ncases)]
    c = 0
    l = 0
    for line in contents:
        cases[c].append(line)
        l += 1
        if l == nlines:
            c += 1
            l = 0
    return cases

def recurs(plates):
    maxi = max(plates)

    if maxi <= 3:
        return maxi

    nSteps = []
    nSteps.append(maxi)
    count = plates.count(maxi)

    for i in range(int((maxi+1)/2), maxi-2):
        subplates = list(filter(lambda x: x != maxi, plates))
        for i in range(count):
            subplates.append(i)
            subplates.append(maxi-i)
            nSteps.append(recurs(subplates))
    return min(nSteps)

def children(config, maxi, count):
    children = []
    base = list(filter(lambda x: x != maxi, config))
    for i in range(int((maxi+1)/2), maxi-1):
        nodes = copy.deepcopy(base)
        for c in range(count):
            nodes.append(i)
            nodes.append(maxi-i)
        children.append(nodes)
    return children



def iterat(plates):
    tree = [[plates]]
    counts = []
    minSteps = 2000

    while True:
        while len(tree[-1]) == 0:
            # go up
            tree.pop()
            if tree == []: return minSteps
            count = counts.pop()

        curNode = tree[-1].pop()
        maxi = max(curNode)
        count = curNode.count(maxi)
        counts.append(count)
        
        minSteps = min(minSteps, (maxi+sum(counts[:-1])))

        if maxi > 3:
            # new level
            tree.append(children(curNode, maxi, count))
        else:
            counts.pop()



def solve(case, c):
    S = case[1].split(' ')
    S = list(map(int, S))
    nSteps = iterat(S)
    print("Case #%d: %d" % (c, nSteps))

fname = "test.in"
cases = readFile(fname)
for c in range(len(cases)):
    solve(cases[c], c+1)
