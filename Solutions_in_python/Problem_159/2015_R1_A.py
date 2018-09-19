
for case in range(int(raw_input())):
    num = raw_input()
    lt = map(int, raw_input().split())
    res1, res2 = 0, 0
    max_eat = 0
    for i in range(len(lt) - 1):
        if lt[i] > lt[i+1]:
            res1 += lt[i] - lt[i+1]
        max_eat = max(max_eat, lt[i] - lt[i+1])
    
    for i in range(len(lt)-1):
        res2 += min(max_eat, lt[i])
        
    print "Case #%d: %d %d" % (case+1, res1, res2)
