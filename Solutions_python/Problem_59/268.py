already = {}
def add(s):
    l = s.split('/')
    b=""
    cnt=0
    for d in l:
        if d!="":
            b+='/'+d
            if already.has_key(b)==False:
                cnt+=1
                already[b]=True
    #print already
    return cnt

T = int(raw_input())
for t in xrange(T):
    already.clear()
    N, M = map(int, raw_input().split())
    for i in xrange(N):
        add(raw_input().strip())
    c=0
    for i in xrange(M):
        c+=add(raw_input().strip())
    print "Case #%d: %d" % (t+1, c)
