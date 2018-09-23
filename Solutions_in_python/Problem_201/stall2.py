t = int(raw_input())
for z in range(1, t + 1):
    s, p = [int(s) for s in raw_input().split(" ")]
    a = []
    a.append(0)
    a.append(0)
    a.append(s)
    for i in range(1, p + 1):
        diff = 0
        for i in range(1, len(a) - 1):
            if((a[i + 1] - a[i] > diff) and (a[i + 1] == s)):
                diff = a[i + 1] - a[i]
                j2 = i + 1
                j1 = i
            if(((a[i + 1] - 1) - a[i] > diff) and (a[i + 1] != s)):
                diff = (a[i + 1] - 1) - a[i]
                j2 = i + 1
                j1 = i
            #if((a[i + 1] - (a[i]) > diff) and (a[i + 1] == s) and (a[i] != 0)):
             #   diff = a[i + 1] - (a[i])
              #  j2 = i + 1
               # j1 = i
           # if(((a[i + 1] - 1) - (a[i]) > diff) and (a[i + 1] != s) and (a[i] != 0)):
            #    diff = (a[i + 1] - 1) - (a[i])
             #   j2 = i + 1
              #  j1 = i
            #print diff,j2,j1,a[j1]
        m = diff / 2
        n = diff % 2
        mid = m + n + a[j1]
        #print mid,a[j1]
        a.insert(j2, mid)
        j2 = j2 + 1
        #print a,a[j2]
    l = (mid - 1) - a[j1]
    if(a[j2] == s):
        r = a[j2] - mid
    else:
        r = (a[j2] - 1) - mid
    minlr = min(l, r)
    maxlr = max(l, r)


    print "Case #{}: {} {}".format(z, maxlr, minlr)
    
