#! /usr/bin/python
'''
Magicka
'''

from collections import defaultdict

T = int(raw_input())

for i in range(T):
    Line = raw_input().split()
    C = int(Line[0])
    combines = defaultdict(dict)

    for j in range(C):
        recipe = Line[j + 1]
        (combines[recipe[0]])[recipe[1]] = recipe[2]
        (combines[recipe[1]])[recipe[0]] = recipe[2]
     
    D = int(Line[C + 1])

    annihilates = defaultdict(set)
    for j in range(C + 2, C + 2 + D):
        recipe = Line[j]
        (annihilates[recipe[0]]).add(recipe[1])
        (annihilates[recipe[1]]).add(recipe[0])

    Charray = Line[C + D + 3]
    
    ptr = 1
    while (ptr < len(Charray)):
        if combines[Charray[ptr]].has_key(Charray[ptr-1]):
            Charray = Charray[:ptr-1] + combines[Charray[ptr]][Charray[ptr-1]] + Charray[ptr+1:]
        elif annihilates[Charray[ptr]].intersection(set(Charray[:ptr])):
            Charray = Charray[ptr+1:]
            ptr = 1
        else:
            ptr += 1

        
    
    print "Case #%d: [%s]" % (i + 1, ', '.join(list(Charray)))

    
