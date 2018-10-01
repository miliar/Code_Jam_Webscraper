t = int(raw_input())
for i in range(0,t):
    ms,shy = raw_input().split()
    ms = int(ms)
    total = 0
    extra = 0
    for shylevel in range(0,ms+1):
        shypeople = int(shy[shylevel])
        if shylevel > total + extra:
            extra += (shylevel - total - extra)
        total = total + shypeople
    print "Case #"+str(i+1)+": " + str(extra)
    
