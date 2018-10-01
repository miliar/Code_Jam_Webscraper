def r1b_1():
    for t in xrange(input()):
        n = input()
        s1 = raw_input()
        s2 = raw_input()
        l1 = len(s1)
        l2 = len(s2)
        i = 0
        j = 0
        first = s1[i]
        res = 0
        flag = 0
        #print s1
        #print s2
        while i < l1 and j < l2:
            c1 = 0
            c2 = 0
            first = s1[i]
            while i < l1 and s1[i] == first:
                i += 1
                c1 += 1
            i -= 1
            while j < l2 and s1[i] == s2[j]:
                j += 1
                c2 += 1
            #print c1,c2
            if c1 == 0 or c2 == 0:
                flag = 1
                break
            res += abs(c1-c2)
            i += 1
        #print i,j
        if i!=l1 or j != l2 or flag:
            print 'Case #%d: Fegla Won'%(t+1)
        else:
            print 'Case #%d: %d'%((t+1),res)
r1b_1()
