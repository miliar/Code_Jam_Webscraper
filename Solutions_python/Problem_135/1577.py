def solve(g1, r1, g2, r2):
    t = set(g1[r1-1])
    s = set(g2[r2-1])
    result = s & t
    if len(result) > 1:
        return "Bad magician!"
    if len(result) == 0:
        return "Volunteer cheated!"
    return str(list(result)[0])
    
ncases = int(raw_input());
for i in xrange(ncases):
    row = int(raw_input())
    grid1 = [[int(a) for a in raw_input().split()] for x in xrange(4)]
    row2 = int(raw_input())
    grid2 = [[int(a) for a in raw_input().split()] for x in xrange(4)]
    print "Case #{}: {}".format(i+1, solve(grid1, row, grid2, row2))