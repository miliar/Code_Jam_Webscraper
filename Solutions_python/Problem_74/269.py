c = int(raw_input())
for case in range(1, c+1):
    line = raw_input().split()
    n = line.pop(0)
    todo = [(line[i],int(line[i+1])) for i in range(0,len(line),2)]
    
    x = {'O':1, 'B':1}
    debt = {'O':0, 'B':0}
    t = 0
    
    for r, p in todo:
        cost = max(abs(p-x[r]) - debt[r], 0) +1
        debt[r] = 0
        x[r] = p
        t += cost
        debt['O' if r=='B' else 'B'] += cost
    print "Case #%d: %d" % (case, t)
