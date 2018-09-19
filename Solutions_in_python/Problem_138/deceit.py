#!/usr/local/bin/python3
#from decimal import *
import sys

# read input
with open(sys.argv[1]) as fd:
    lines = fd.read().split("\n")
    if lines[-1] == "": lines = lines[:-1]

def mapper(line):
    # return sorted(map(float, line.split(" ")), reverse=True)
    # sort blocks by ascending weight
    return sorted(map(float, line.split(" ")), reverse=False)

class Case(object):
    def __init__(self, lines):
        lines = lines[:]
        self.blocks = int(lines.pop(0))
        self.naomi = mapper(lines.pop(0))
        self.ken = mapper(lines.pop(0))

def honest(case):
    case = Case(case)
    wins = 0
    #print("\nPlaying War.")
    for _ in range(case.blocks):
        # Naomi chooses her lightest block
        naomiBlock = case.naomi.pop(0)
        #print("Naomi chooses {}.".format(naomiBlock))
        for i in range(len(case.ken)):
            # Ken chooses his lightest block that beats Naomi's
            if case.ken[i] > naomiBlock or i == len(case.ken) - 1:
                kenBlock = case.ken.pop(i)
                #print("Ken chooses {}.".format(kenBlock))
                break
        if naomiBlock > kenBlock:
            wins += 1
    return wins

def deceit(case):
    case = Case(case)
    wins = 0
    #print("\nPlaying Deceitful War.")
    #print("Naomi", case.naomi)
    #print("Ken  ", case.ken)
    for _ in range(case.blocks):
        if case.naomi[-1] < case.ken[-1]:
            # Naomi chooses her lightest block and lies
            naomiBlock = case.naomi.pop(0)
            #print("Naomi chooses {}.".format(naomiBlock))
            if len(case.ken) > 1:
                diff = (case.ken[-1] - case.ken[-2])/2
                naomiLie = case.ken[-2] + diff
            else:
                naomiLie = naomiBlock
            #print("Naomi claims {}.".format(naomiLie))
            firstRun = False
        else:
            # Naomi chooses her heaviest block
            naomiBlock = case.naomi.pop()
            #print("Naomi chooses {}.".format(naomiBlock))
            naomiLie = naomiBlock
        for i in range(len(case.ken)):
            # Ken chooses his lightest block that beats the lie
            if case.ken[i] > naomiLie or i == len(case.ken) - 1:
                kenBlock = case.ken.pop(i)
                #print("Ken chooses {}.".format(kenBlock))
                break
        if naomiBlock > kenBlock:
            #print("Naomi wins!")
            wins += 1
        else:
            #print("Ken wins!")
            pass
    return wins

# parse input
numCases = int(lines.pop(0))
cases = [lines[3*i:3*i+3] for i in range(numCases)]

for i, case in enumerate(cases):
    honestTrial = honest(case)
    deceitTrial = deceit(case)
    #print()
    print("Case #{0}: {1} {2}".format(i+1, deceitTrial, honestTrial))
