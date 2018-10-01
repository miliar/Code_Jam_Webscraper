def invert(ch):
    if ch=='+':
        return '-'
    elif ch=='-':
        return '+'
    else:
        return '?'
def f(D,N):
    horses = []
    max_time = 0
    for i in xrange(N):
        pos,speed = map(int,raw_input().split(' '))
        max_time = max(max_time, (D-pos)*1./speed)
    
    return D/max_time
        
    
    
        
T = int(raw_input())
for i in xrange(1,T+1):
    print "Case #%d: %.8f" % (i, f(*map(int,raw_input().split())))
    
    # 5
    # 0
    # 1
    # 2
    # 11
    # 1692Square Brackets [ ] | English Club