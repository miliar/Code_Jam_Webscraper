for t in range(int(raw_input())):
    name, n = [i for i in raw_input().split()]
    n = int(n)
    
    consecutive = [False]*len(name)
    for i in range(len(name)-n+1):
        consonant = True
        for j in range(i, i+n):
            if name[j] == 'a' or name[j] == 'e' or name[j] == 'i' or name[j] == 'o' or name[j] == 'u':
                consonant = False
                break
        consecutive[i] = consonant
    
    value = 0
    for i in range(len(name)-n+1):
        for j in range(len(name), i+n-1, -1):
            if True in consecutive[i:j-n+1]: value += 1
    
    print "Case #%d: %d" % (t+1, value)
