T = input()   
    
for tc in range(T):
    A = input()
    arr = map(int, raw_input().split())

    M = max(arr)
    ret = M    
    for i in range(2, M):
        c = i
        for n in arr:
            c += (n-1)/i
        ret = min(ret, c)

    print "Case #" + str(tc+1) + ": " + str(ret)
#    print "Case #" + str(tc+1) + ": " + str(f(arr))
