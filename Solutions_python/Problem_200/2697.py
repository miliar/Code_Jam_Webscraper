t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
#  n, m = [s for s in raw_input().split(" ")]
    x = raw_input()
    n = list(x)
    bp = -1
    sp = -1
    for j in xrange(len(n)-1):
        if (n[j]<=n[j+1]):
            sp = j
            if (n[j] != n[j+1]):
                bp=j
        else:
            break

#bp = first not j < j +1 fill point
#sp = first j > j + 1 check if already answer
        
    #112bp3333333sp2222220
    #112bp2999999sp9999999

    #1bp1111111sp0
    #0bp9999999sp9
    if ( sp != len(n) - 2 ):
        bp=bp+1
        n[bp] = str(int(n[bp])-1)
        for j in reversed(xrange(bp+1,len(n))):
            n[j]='9'
#    print bp, sp
    print "Case #{}: {}".format(i, str(int("".join(n))))
