

T = int(raw_input())
for c in xrange(T):
    l = map(int, raw_input().strip().split())
    print "Case #%d:"%(c+1),
    N, S, p, t = l[0], l[1], l[2], l[3:]
    good, req = 0, 0
    for ti in t:
        if ti >= 3*p: good += 1
        elif 3*p-2<=ti and ti>=1: good += 1
        elif 3*p-4<=ti<=3*p-3 and ti>=2: req += 1
    print good + min(req, S)
    
