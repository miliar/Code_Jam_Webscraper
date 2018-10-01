

def bfs(i, j, cake, cc, dir):
    if i < 0 or i >= len(cake) or j < 0 or j >= len(cake[0]):
        return
    if cake[i][j] == '?':
        cake[i][j] = cc
        if dir == 1:
            bfs(i - 1, j, cake, cake[i][j], 1)
            bfs(i + 1, j, cake, cake[i][j], 1)
        else:
            bfs(i, j - 1, cake, cake[i][j], 2)
            bfs(i, j + 1, cake, cake[i][j], 2)



def solve(cake):

    for i in range(len(cake)):
        for j in range(len(cake[0])):
            if cake[i][j] != '?':
                bfs(i - 1, j, cake, cake[i][j], 1)
                bfs(i + 1, j, cake, cake[i][j], 1)
    for i in range(len(cake)):
        for j in range(len(cake[0])):
            if cake[i][j] != '?':         
                bfs(i, j - 1, cake, cake[i][j], 2)
                bfs(i, j + 1, cake, cake[i][j], 2)
        
    return
    
t=int(raw_input())
for cas in xrange(1,t+1):
    sss=str(raw_input())
    arra = sss.split()
    rr = int(arra[0])
    cc = int(arra[1])
    cake = []
    for ii in range(rr):
        cake.append(list(str(raw_input())))
    print "Case #{}:".format(cas)
    solve(cake)
    for iii in range(rr):
        print ''.join(cake[iii])
