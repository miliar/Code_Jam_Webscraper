
T = int(input())
for case in range(T):
    vals = input().split()
    C,R = int(vals[0]),int(vals[1])
    
    cake = []
    for r in range(C):
        cake.append(list(input()))
        
    letpostions = [(c,r) for r in range(R) for c in range(C) if cake[c][r] != "?"]
    for letp in letpostions:
        initc = letp[0]
        initr = letp[1]
        endc = C-1
        endr = R-1
        startc = 0
        startr = 0

        for c in range(initc+1,C):
            if cake[c][initr] != "?":
                endc = c-1
                break
        
        for c in range(initc-1,-1,-1):
            if cake[c][initr] != "?":
                startc = c+1
                break
                
        def check_col(r):
            for c in range(startc,endc+1):
                if cake[c][r] != "?":
                    return False
            return True
                
        for r in range(initr+1,R):
            if not check_col(r):
                endr = r-1
                break
        
        for r in range(initr-1,-1,-1):
            if not check_col(r):
                startr = r+1
                break
                
        for c in range(startc,endc+1):
            for r in range(startr,endr+1):
                cake[c][r] = cake[initc][initr]
                
    cakestr = "\n".join("".join(l) for l in cake)
    print("Case #{}:\n{}".format(case+1,cakestr))