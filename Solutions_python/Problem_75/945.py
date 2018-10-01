import sys
fp = file(sys.argv[1])
#fp = open("test.in")

#read nb of cases
T = int(fp.next())

for i in range(T):
    line = list(fp.next().split())
    C = int(line[0])
    D = int(line[C+1])
    N = int(line[C+D+2])
    combine = {}
    oppose = {}

    for j in range(1,C+1,1):
        s = line[j]
        p = s[:-1]
        anti_p = p[::-1]
        combine[p] = s[2]
        combine[anti_p] = s[2]
    for j in range(C+2,C+D+2,1):
        s = line[j]
        if(s[0] in oppose.keys()):
            oppose[s[0]].append(s[1])
        else:
            oppose[s[0]] = [s[1]]
        if(s[1] in oppose.keys()):
            oppose[s[1]].append(s[0])
        else:
            oppose[s[1]] = [s[0]]

    elements = list(line[C+D+3])
    final = []

    while len(elements)>0:
        if(len(final) == 0):
            final.append(elements.pop(0))
            continue
        pop_elem = elements.pop(0)
        last_elem = final[-1]
        seq = last_elem+pop_elem
        if(seq in combine.keys()):
            new_elem = combine[seq]
            elements.insert(0,new_elem)
            final = final[:-1]
            continue
        else:
            if(pop_elem in oppose.keys()):
                opposed_elems = oppose[pop_elem]
                for test in opposed_elems:
                    if(test in final):
                        final = []
                        break
        if(len(final)>0):
            final.append(pop_elem)
    print "Case #%d: %s" % (i+1, str(final).replace('\'',''))
    
fp.close()
