T = int(raw_input())  

for K in xrange (T):
    n, p = [int(i) for i in raw_input().split(" ")]
    g = [int(i) for i in raw_input().split(" ")]

    residue = [0] * p
    for i in xrange(n):
        residue[g[i] % p] += 1
    #print residue

    ans = residue[0]

    if (p == 2):
        ans += residue[1] / 2
        if residue[1] % 2:
            ans += 1
    elif (p == 3):
        r = min(residue[1], residue[2])
        residue[1] -= r
        residue[2] -= r
        ans += r + residue[1] / p + residue[2] / p
        if (residue[1] % 3 or residue[2] % 3):
            ans += 1
    else:
        r = min(residue[1], residue[3])
        ans += r
        residue[1] -= r
        residue[3] -= r
        ans += (residue[1] + residue[3]) / p + residue[2] / 2
        r = (residue[1] + residue[3]) % p
        #print r, residue
        if residue[2] % 2: 
            if r > 2:
                ans += 1
            ans += 1
        elif r > 0:
            ans += 1

    print "Case #{}: {}".format(K + 1, ans)