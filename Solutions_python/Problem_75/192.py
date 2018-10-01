#!/usr/bin/python

def solve(line):

    line = line.split()

    i = 0
    # Read first the Construction Rules
    CRules = []
    C = int(line[i])
    i += 1
    while len(CRules)<C:
        s = line[i]
        i += 1
        # Each construction is [ 'aba', 'c' ] 
        CRules.append( [ s[0:2]+s[0], s[2]] )

    # Now the destruction
    DRules = []
    D = int(line[i])
    i += 1
    while len(DRules)<D:
        s = line[i]
        i += 1
        # Each destruction is [ 'ab' ]
        DRules.append( s[0:2] )
    
    # Finally, the case
    N = int(line[i])
    if N==0:
        return "[]"
    i += 1
    spell = line[i]
    # Small check to avoid surprises
    assert(len(spell)==N)

    # Now apply the letters of the spell one by one
    res = []
    for s in spell:
        finish = False
        new = s            
        while not (finish or len(res)==0):
            # Construct the candidate
            candidate = res[-1]+new

            # Apply the constructions
            reloop = False
            for rule in CRules:
                if candidate in rule[0]:
                    del res[-1]
                    new = rule[1]
                    reloop = True
                    break
            if reloop:
                # A construction rule applied =>
                # return to the candidate creation
                break
            # Appetite for destrution!
            for rule in DRules:
                if rule[0]==new:
                    pair = rule[1]
                elif rule[1]==new:
                    pair = rule[0]
                else:
                    continue
                if pair in res:
                    res = []
                    new = None
                    break
            # 
            finish = True
        # Add the new element... if any    
        if new is not None:
            res.append(new)
    # Format the result according to the needed output
    s = reduce(lambda s,c: s+" "+c+",", res, "")
    return "[" + s[1:-1] + "]"


import sys

if len(sys.argv)<2:
    fd = sys.stdin
else:
    fd = open(sys.argv[1], 'r')

T = int(fd.readline().strip('\n'))
i = 1
for line in fd:
    print("Case #%d: %s" % (i, solve(line)))
    i += 1
    if i>T:
        break

fd.close()
