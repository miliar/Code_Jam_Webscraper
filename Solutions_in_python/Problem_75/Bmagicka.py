#!/usr/bin/python3

from sys import argv

from collections import defaultdict
def hash(): return defaultdict(hash)

def addit(combine, oppose, result, char):
    if len(result) == 0:
        result.append(char)
    else:
        lastchar = result[-1]
        if lastchar in combine and char in combine[lastchar]:
            result[-1] = combine[lastchar][char]
            return
        else:
            for prev in result:
                if prev in oppose and char in oppose[prev]:
                    while len(result) > 0:
                        result.pop()
                    return
        result.append(char)

infile = open(argv[1])
cases = int(infile.readline())
for i in range(0, cases):
    line = infile.readline().rstrip('\n')
    vals = line.split()
    c = int(vals[0])
    vals = vals[1:]
    combine = hash()
    oppose  = hash()
    for j in range(0,c):
        combine[vals[0][0]][vals[0][1]] = vals[0][2]
        combine[vals[0][1]][vals[0][0]] = vals[0][2]
        vals = vals[1:]
    d = int(vals[0])
    vals = vals[1:]
    for j in range(0,d):
        oppose[vals[0][0]][vals[0][1]] = True
        oppose[vals[0][1]][vals[0][0]] = True
        vals = vals[1:]
    vals = vals[1:]
    string = vals[0]
    result = []
    for char in string:
        addit(combine, oppose, result, char)
    print('Case #{}: [{}]'.format(i+1, ', '.join(result)))
