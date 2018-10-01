fin = file("B-large.in", "rU")
fout = file("B-large.out", "w")
ncases = int(fin.readline().strip())
for i in xrange(ncases):
    line = fin.readline().split()
    currpos = 0
    
    ncombine = int(line[0])
    combinelist = line[1:1+ncombine]
    noppose = int(line[1+ncombine])
    opposelist = line[2+ncombine:2+ncombine+noppose]
    ninvoke = int(line[2+ncombine+noppose])
    invokelist = line[3+ncombine+noppose:]
    if len(invokelist) == 1: #0 check
        invokelist = invokelist[0]
    else:
        invokelist = ''
    #print ncombine, combinelist, noppose, opposelist, ninvoke, invokelist

    combinedict = {} #dictionaries inside dictionaries
    for group in combinelist:
        #make both ways
        if group[0] not in combinedict:
            combinedict[group[0]] = {}
        combinedict[group[0]][group[1]] = group[2]
        if group[1] not in combinedict:
            combinedict[group[1]] = {}
        combinedict[group[1]][group[0]] = group[2]
        
    opposedict = {} #dictionary of sets
    for group in opposelist:
        #make both ways
        if group[0] not in opposedict:
            opposedict[group[0]] = set()
        opposedict[group[0]].add(group[1])
        if group[1] not in opposedict:
            opposedict[group[1]] = set()
        opposedict[group[1]].add(group[0])

    #print combinedict, opposedict

    stack = []
    for lett in invokelist:
        stack.append(lett)
        while True: #recursive combine
            if len(stack) >= 2 and stack[len(stack)-1] in combinedict and \
               stack[len(stack)-2] in combinedict[stack[len(stack)-1]]:
                #ie. there exists a combine
                newlett = combinedict[stack[len(stack)-1]][stack[len(stack)-2]]
                stack = stack[:-2]
                stack.append(newlett)
            else:
                break
        #check for opposes against last letter
        reset = False
        if stack[len(stack)-1] in opposedict:
            for lett in stack:
                if lett in opposedict[stack[len(stack)-1]]:
                    reset = True
                    break
        if reset:
            stack = []
    #print stack
    strout = 'Case #' + str(i+1) + ': ['
    for i in xrange(len(stack)):
        strout += stack[i]
        if i != len(stack) - 1:
            strout += ', '
    strout += ']\n'
    #print strout
    fout.write(strout)
fin.close()
fout.close()
