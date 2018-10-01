_case = 0
def gout(s):
    global _case
    _case += 1
    print "Case #%d: %s" % (_case,s) 

def memoize(f):
    dict = {}
    def func(*n):
        if n in dict:
            return dict[n]
        else:
            dict[n] = f(*n)
            return dict[n]
    return func

for _ in xrange(int(raw_input())):
    line = raw_input().split()
    nCombos = int(line[0])
    nWipes = int(line[nCombos+1])
    combos = {}
    wipes = {}
    for combo in line[1:nCombos+1]:
        combos[(combo[0],combo[1])] = combo[2]
        combos[(combo[1],combo[0])] = combo[2]
    for wipe in line[nCombos+2:nCombos+2+nWipes]:
        if wipe[0] not in wipes:
            wipes[wipe[0]] = set()
        if wipe[1] not in wipes:
            wipes[wipe[1]] = set()
        wipes[wipe[0]].add(wipe[1])
        wipes[wipe[1]].add(wipe[0])
    
    pile = []
    for c in line[-1]:
        pile.append(c)
        while len(pile)>1 and (pile[-2],pile[-1]) in combos:
            toInsert = combos[(pile[-2],pile[-1])]
            pile.pop()
            pile.pop()
            pile.append(toInsert)
        if pile[-1] in wipes and any((c in wipes[pile[-1]] for c in pile[:-1])):
            pile = []
    gout('['+', '.join(pile)+']')
