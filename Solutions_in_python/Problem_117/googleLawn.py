T = int(raw_input())
for t in range(1,T+1):
    n,m = [int(x) for x in raw_input().split()]
    field = [[int(x) for x in raw_input().split()] for x in range(n)]
    horizontalMaxs = [max(row) for row in field]
    verticalMaxs = [max(row[i] for row in field) for i in range(m)]
    canMake = True
    for i in range(n):
        for j in range(m):
            if field[i][j]< min(horizontalMaxs[i],verticalMaxs[j]):
                canMake = False
    print "Case #"+str(t)+":",
    if canMake:
        print "YES"
    else:
        print "NO"
