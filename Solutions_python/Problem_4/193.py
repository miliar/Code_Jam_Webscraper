n = input()
for i in range(n):
#    print i
    lnum = input()
    l1 = []
    l2 = []
    n1 = raw_input()
#    print n1
    for w in n1.split():
        l1 += [int(w)]
    n1 = raw_input()
#    print n1
    for w in n1.split():
        l2 += [int(w)]
#    print l1,l2
    l1.sort()
    l2.sort(None,None,True)
 #   print l1,l2
    ans =0
    for l in range(lnum):
        ans += l1[l] * l2[l]
    print "Case #%d: %d" %(i+1, ans)
        
