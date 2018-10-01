k = input()
for j in xrange(k):
    r = 0
    a = [int(i) for i in raw_input().split()]
    while a[0] < a[1]:
        h = {}
        s1 = str(a[0])
        tmp = a[0]+1
        while tmp <= a[1]:
            s2 = str(tmp)
            for i in xrange(1,len(s2)):
                if s1 == s2[i:]+s2[:i]:
                    if not((s1, s2) in h or (s2,s1) in h):
                        r+=1
                        h[(s1,s2)] = 1
            tmp+=1
        a[0]+=1
    print "Case #"+str(j+1)+": "+str(r)
