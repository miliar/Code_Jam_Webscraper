def solve(ix):
    C, F, X = map(float, raw_input().strip().split())
    rt = 2.0
    past = 0.0
    while True:
        t0 = past + X / rt 
        t1 = past + C / rt + X / (rt+F)
        if t1 < t0:
            past += C / rt
            rt += F
        else:
            ans = t0    
            break
    print 'Case #%d: %.7f' % (ix, ans)   

N = int(raw_input())
for ix in range(N):
    solve(ix+1)
