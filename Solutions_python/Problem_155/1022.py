import sys

test_cases = int(sys.stdin.readline().strip("\n"))

for tc in range(1, test_cases+1):
    smax, aud = sys.stdin.readline().strip("\n").split()
    smax = int(smax)
    
    stand = 0
    add = 0
    for i in range(smax+1):
        cur = int(aud[i])
        if cur > 0:
            if stand < i:
                add += i - stand
                stand += add
        stand += cur
        
    print "Case #%d: %d" % (tc, add)
