ent = input()
for p in range(0, ent):
    array = map(int, raw_input().split())
    n = array[0]
    k = array[1]

    s = []
    s.append(n/2)
    s.append(n-s[0]-1)
    k -= 1

    x = s[0]
    y = s[1]
    
    while (k > 0):
        s.sort()
        last = len(s)-1
        x = s[last]/2
        y = s[last]-x-1
        s[last] = x
        s.append(y)
        k -= 1
    
    
    print "Case #%d: %d %d" % (p+1, max(x, y), min(x, y))
