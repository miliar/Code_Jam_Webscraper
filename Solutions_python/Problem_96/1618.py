fp = open('inputs.txt', 'r')
inputs = fp.readlines()
fp.close()
fp = open('output.txt', 'w')
cases = int(inputs[0].strip('\n'))
for i in range(1, cases + 1):
    triplets = {}
    shocks = {}
    line = inputs[i].strip('\n').split()
    n = int(line[0])
    s = int(line[1])
    p = int(line[2])
    # scores
    for j in range(3, len(line)):
        for a in range(0, int(int(line[j]) / 2) + 1):
            for b in range(a, a + 3):
                for c in range(a, a + 3):                    
                    if a + b + c == int(line[j]): # we got a triplet
                        if max(a, b, c) - a == 2:
                            try:
                                if shocks[j][2] > max(b, c):
                                    shocks[j] = sorted([a, b, c])
                            except KeyError:
                                shocks[j] = sorted([a, b, c])
                            continue
                        try:                        
                            if max(a, b, c) > triplets[int(line[j])][2]:
                                triplets[j] = sorted([a, b, c])    
                        except KeyError:
                            triplets[j] = sorted([a, b, c])

    shocks_pref   = 0
    triplets_pref = 0
    both          = 0
    np            = 0

    for x in triplets:
        try:
            if triplets[x][2] >= p and shocks[x][2] < p:
                triplets_pref += 1        
            elif triplets[x][2] < p and shocks[x][2] >= p:
                shocks_pref   += 1
            elif triplets[x][2] >= p and shocks[x][2] >= p:
                both += 1
            else:
                np += 1
        except KeyError:
            if triplets[x][2] >= p:
                triplets_pref += 1
            else:
                np += 1
    if shocks_pref >= s:
        res = s + both + triplets_pref
    else:
        res = both + shocks_pref + triplets_pref
    fp.write('Case #%d: ' % i + str(res) + '\n')
    print str(triplets)
    print str(shocks)
    print 'Both ', both, ' Triplets ', triplets_pref, ' Shocks ', shocks_pref, ' Res ', res
