N = input()
for tc in range(1, N+1):
    c, f, x = map(float, raw_input().split())
    n = int((x*f - 2*c)/(c*f))
    t = 0.0
    
    n = max(0, n)
    
    for i in range(n):
        t += c/(2 + i*f)
    
    t += x / (2 + n*f)
    
    print "Case #%d: %.7f"%(tc, t)