for t in range(int(raw_input())):
    n = list(raw_input().strip())
    sw = 1
    while sw:
        sw = 0
        for i in range(len(n)-1):
            if n[i+1] < n[i]:
                n[i] = chr(ord(n[i])-1)
                for j in range(i+1, len(n)):
                    n[j] = "9"
                sw = 1    
    if n[0] == "0":
        del n[0]
    print "Case #%d: %s"%(t+1, "".join(n))    
    
