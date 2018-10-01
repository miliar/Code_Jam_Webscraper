T = int(raw_input())  

for K in xrange (T):
    r, c = [int(g) for g in raw_input().split(" ")]
    s = []
    for g in xrange(r):
        s.append(raw_input())
    ans = ""

    columnHasCake = [False] * c
    rowSplit = []
    for i in xrange(r):
        for j in xrange(c):
            if s[i][j] != '?':
                if columnHasCake[j]:
                    rowSplit.append(i - 1)
                    columnHasCake = [g != '?' for g in s[i]]
                    break;
                else:
                    columnHasCake[j] = True
    rowSplit.append(r - 1)
    #print rowSplit

    cutFrom = 0
    for k in xrange(len(rowSplit)):
        cut = rowSplit[k]
        columnSplit = []
        initial = []
        for j in xrange(c):
            for i in xrange(cutFrom, cut + 1):
                if s[i][j] != '?':
                    columnSplit.append(j)
                    initial.append(s[i][j])
                    break
        #print cut, columnSplit, initial

        if initial:
            row = ""
            j = 0
            while columnSplit:
                row += initial[0]
                j += 1
                if j > columnSplit[0]:
                    last = initial.pop(0)
                    columnSplit.pop(0)
                #print j, initial, columnSplit
            while j < c:
                row += last
                j+= 1

            for i in xrange(cutFrom, cut + 1): 
                ans += '\n' + row
        else:
            for i in xrange(cutFrom, r): 
                ans += '\n' + row

        cutFrom = cut + 1





    print "Case #{}: ".format(K+1)
    print ans.strip("\n")
