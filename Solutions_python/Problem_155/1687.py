t = int(raw_input())
for tt in range(t) :
    s = raw_input().split()
    x = int(s[0])
    y = [int(i) for i in s[1]]
    a = y[0]
    ans = 0
    for i in range(1,x+1) :
        if a >= i :
            a = a + y[i]
        else :
            p = i-a
            ans = p + ans 
            a = a + p + y[i]
    print "Case #" + str(tt+1) + ": " + str(ans)