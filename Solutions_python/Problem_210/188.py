t = int(input())

for i in range(1, t+1):
    Ac, Aj = [int(x) for x in input().split()]
    
    ct = 0
    jt = 0
    
    A = []
    
    for j in range(Ac):
        c, d = [int(x) for x in input().split()]
        A.append((c,d,0))
        ct = ct + d - c
    for j in range(Aj):
        j, k = [int(x) for x in input().split()]
        A.append((j,k,1))
        jt = jt + k - j
    
    A.sort()
    
    gt = 0
    bt = ([], [])
    
    last = A[0]
    tmp = A[-1]
    
    if tmp[2] != last[2]:
        gt = last[0] - tmp[1] + 1440
        y = 1
    else:
        bt[tmp[2]].append(last[0] - tmp[1] + 1440)
        y = 0
        
    for block in A[1:]:
        if last[2] != block[2]:
            gt = gt + block[0] - last[1]
            y = y + 1
            last = block
        
        else:
            bt[last[2]].append(block[0] - last[1])
            last = block
            
    if not (ct + gt >= 720 and jt + gt >= 720):
        bt[0].sort(reverse = True)
        bt[1].sort(reverse = True)
        
        y0 = 0           
        y1 = 0
        t0 = 720 - ct - gt
        t1 = 720 - jt - gt
        
        for tic in bt[1]:
            y0 = y0 + 2
            t0 = t0 - tic
            if t0 <= 0:
                break
            
        for tic in bt[0]:
            y1 = y1 + 2
            t1 = t1 - tic
            if t1 <= 0:
                break
            
        if t0 > 0 or ct + gt >= 720:
            y = y + y1
        elif t1 > 0 or jt + gt >= 720:
            y = y + y0
        else:
            y = y + min(y0,y1)
    
    print("Case #{}: {}".format(i, y))