f = open("C-small-attempt0.in")
fOut = open("C-small-attempt0.out", "w")

readIntVec = lambda f: [int(x) for x in f.readline().strip().split()]


T = int(f.readline().strip())

for tc in range(T):
    R, k, N = readIntVec(f)
    v = readIntVec(f)

    ans = 0
    g = 0
    for t in range(R):
        g0 = g
        s = v[g]
        g = (g + 1) % N
        
        while g != g0 and (s + v[g]) <= k:
            s += v[g]
            g = (g + 1) % N

        ans += s
            
    fOut.write("Case #%d: %d\n" % (tc + 1, ans))
    

fOut.close()
f.close()

