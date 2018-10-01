test = int(raw_input())
for _ in xrange(test):
    s,k = raw_input().strip().split()
    s,k = list(s),int(k)
    count = 0
    for i in xrange(len(s)-k+1):
        if s[i] == '-':
            for m in xrange(i,i+k):
                if s[m] == '-':
                    s[m] = '+'
                else:
                    s[m] = '-'
            count += 1
#            print(s)
    if '-' in s:
        print "Case #"+str(_+1)+": IMPOSSIBLE"
    else:
        print "Case #"+str(_+1)+": "+str(count)
        
