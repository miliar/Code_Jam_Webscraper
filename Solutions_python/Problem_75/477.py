#!/usr/bin/env python

from sys import stdin
#from math import abs

lines = stdin.readlines()
T = int(lines[0])
lines = lines[1:]

for t in range(0,T):
    L = lines[t].split()

    C = int(L[0])
    
    i = 1 # index in of next unread element in L

    # read compatible (combinable) elements
    combine = {}
    for c in range(i,i+C):
        x = L[c]
        # and they combine to x[2]
        combine[x[0],x[1]] = x[2]
        combine[x[1],x[0]] = x[2]
    i += C

    # read opposite elements
    opposed = {}
    D = int(L[i])
    i += 1
    for d in range(i,i+D):
        X = tuple(L[d])
        for x in X:
            if x not in opposed:
                opposed[x] = set(())
        x,y = X
        opposed[x].add(y)
        opposed[y].add(x)

    i += D
    N = L[i]
    queue = L[i+1] # elements to be invoked

    elems = []      # element list
    seen  = set(()) # base elements in the list
    count = {}      # number of instances of each base element in the list
    for e in queue:
        end = None # element at the end of the element list
        if len(elems) != 0:
            end = elems[-1]
        ## invoke element
        # combine?
        if (e,end) in combine:
            elems.pop()
            count[end] -= 1
            if count[end] == 0:
                seen.remove(end)
            elems.append(combine[e,end])
        # clear?
        elif e in opposed and len(opposed[e] & seen) > 0:
            elems = []
            seen  = set(())
            count = {}
        # normal
        else:
            elems.append(e)
            seen.add(e)
            if e not in count:
                count[e] = 0
            count[e] += 1
    result = ", ".join(elems)
   
    print("Case #{0}: [{1}]".format(t+1, result))
