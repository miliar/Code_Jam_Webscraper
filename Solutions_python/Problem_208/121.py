# Google Codejam 2017: Round 1B
# Problem C: Pony Express
# Author: Mahmoud Aladdin <aladdin3>

import sys

INF = 1 << 70

def solve(cn):
    n, q = map(int, raw_input().strip().split())
    
    horses = []
    for i in xrange(n):
        ei, si = map(int, raw_input().strip().split())
        horses.append((ei, si))
    
    grid = []
    for i in xrange(n):
        grid.append(list(map(int, raw_input().strip().split())))
        for j in xrange(n):
            if grid[i][j] == -1:
                grid[i][j] = INF
        
    
    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])

    times = []
    for i in xrange(n):
        times.append([])
        for j in xrange(n):
            if grid[i][j] <= horses[i][0]:
                times[-1].append(grid[i][j] / float(horses[i][1]))
            else:
                times[-1].append(float(INF))
    
    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                times[i][j] = min(times[i][j], times[i][k] + times[k][j])    
    
    solution = []
    for i in xrange(q):
        ui, vi = map(int, raw_input().strip().split())
        solution.append(times[ui - 1][vi - 1])
    
    print "Case #{0}: {1}".format(cn, " ".join(map(str, solution)))
    print >>sys.stderr, "Case #{0}".format(cn)
        

if __name__ == "__main__":
    cn = input()
    for i in xrange(cn):
        solve(i + 1)