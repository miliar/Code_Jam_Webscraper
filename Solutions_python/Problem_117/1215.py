data = open("P2_large.txt")
out = open("P2.out","w")

cases = int(data.readline())
for case in xrange(cases):
    m,n = map(int,data.readline().split())
    grid = []
    for _ in xrange(m):
        grid.append(map(int,data.readline().split()))
    #for row in grid: print row
    
    col_max = [0]*n
    row_max = [0]*m
    for i in xrange(m):
        row_max[i] = max(grid[i])
    for j in xrange(n):
        for i in xrange(m):
            col_max[j] = max(col_max[j],grid[i][j])
    #print row_max
    #print col_max
    
    ok = True
    for i in xrange(m):
        for j in xrange(n):
            if grid[i][j] < col_max[j] and grid[i][j] < row_max[i]:
                ok = False
                break
        if not ok:
            break
    
    out.write("Case #%i: " %(case+1)) 
    if ok:
        out.write("YES\n")
        print "YES"
    else:
        out.write("NO\n")
        print "NO"
    #print "\n"