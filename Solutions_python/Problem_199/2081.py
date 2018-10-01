n = int(raw_input())
for i in range(n):
    r = raw_input().split()
    s = list(r[0])
    k = int(r[1])
    c = 0
    
    for ptr in range(0, len(s)-k+1):
        if s[ptr] == "+":
            continue
        
        c += 1
        for q in range(k):
            if s[ptr+q] == "-":
                s[ptr+q] = "+"
            else:
                s[ptr+q] = "-"
                
    for ptr in range(len(s)-k+1, len(s)):
        if s[ptr] == "-":
            print "Case #"+str(i+1)+": IMPOSSIBLE"
            break
    else:
        print "Case #"+str(i+1)+":", c
