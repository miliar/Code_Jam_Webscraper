infile = open("B-large.in")
outfile = open("B-large.out","w")
T = int(infile.readline())
for t in range(1,T+1):
    N, M = map(int, infile.readline().split())
    #print(N,M)
    yard = []
    for _ in range(N):
        yard.append(map(int, infile.readline().split()))
    able = True
    while yard:
        minval = min([min(x) for x in yard])
        rows = []
        cols = []
        for i in range(N):
            if all(x == minval for x in yard[i]):
                rows.append(i)
        for j in range(M):
            if all(yard[y][j] == minval for y in range(N)):
                cols.append(j)
        changed = False
        for r in sorted(rows, reverse=True):
            yard.pop(r)
            N -= 1
            changed = True
        for c in sorted(cols, reverse=True):
            for i in range(N):
                yard[i].pop(c)
            M -= 1
            changed = True
        #print minval, yard
        if not changed:
            able = False
            break
    ans = "YES"
    if not able:
        ans = "NO"
    #print ans
    outfile.write("Case #{}: {}\n".format(t, ans))

infile.close()
outfile.close()
    
        
