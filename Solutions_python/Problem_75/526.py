# Google Code Jam 2011 qualifying round.

import sys
def invoke(list, element, combines, opposed):
    if not list:
        return [element]
    pair = [list[-1],element]
    pair.sort()
    pair = tuple(pair)
    if pair in combines:
        list.pop()
        return list + [combines[pair]]
    for a in list:
        if (a,element) in opposed:
            return []
    return list + [element]

def run():
    file = open(sys.argv[1])
    numCases = int(file.readline())
    for case in range(1, numCases+1):
        line = file.readline().split()
        combines = {}
        for i in range(int(line.pop(0))):
            comb = line.pop(0)
            pair = [x for x in comb[:2]]
            pair.sort()
            combines[tuple(pair)] = comb[2]
        opposed = {}
        for i in range(int(line.pop(0))):
            opp = line.pop(0)
            opposed[(opp[0],opp[1])] = 1
            opposed[(opp[1],opp[0])] = 1
        list = []
        for e in line[-1]:
            list = invoke(list, e, combines, opposed)
        print 'Case #{0}: {1}'.format(case, list).replace("'","")
run()
