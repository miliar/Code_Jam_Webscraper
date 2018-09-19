def getBinRep(x,size):
    bits = []
    while(x):
        bits.append( x % 2)
        x /= 2
    bits.extend( [0] * (size - len(bits)) )
    return list(reversed(bits))

t = int(raw_input())
for tc in range(t):
    n = int(raw_input())
    s = map (int, raw_input().split())

    current_max = 0

    for iterator in range(1, 2**n -1):
        left, right = 0,0
        leftsum, rightsum = 0,0
        bin = getBinRep(iterator,n)
        
        for i in range(len(bin)):
            if bin[i] == 0:
                left ^= s[i]
                leftsum += s[i]
            else:
                right ^= s[i]
                rightsum += s[i]
        if left == right:
            if max(leftsum, rightsum) > current_max:
                current_max = max(leftsum, rightsum)

    if current_max == 0:
        print "Case #%d: NO" % (tc + 1)
    else:
        print "Case #%d: %d" % (tc + 1, current_max)
