def solve(x, r, c):
    if (x == 1):
        return 1
    if (x == 2):
        a = [[0,1,0,1],[1,1,1,1],[0,1,0,1],[1,1,1,1]]
        return a[r-1][c-1]
    if (x == 3):
        a = [[0,0,0,0],[0,0,1,0],[0,1,1,1],[0,0,1,0]]
        return a[r-1][c-1]
    a = [[0,0,0,0],[0,0,0,0],[0,0,0,1],[0,0,1,1]]
    return a[r-1][c-1]

readfile = open("D-small-attempt0.in", "r")
T = int(readfile.readline())
putfile = open("d.out", "w")
C = 0
for data in readfile.readlines():
    data = data.strip('\n')
    x, r, c = data.split(' ')
    ans = solve(int(x), int(r), int(c))
    C = C+1
    if (ans == 1):
        putfile.write("Case #%d: GABRIEL\n"% C)
    else:
        putfile.write("Case #%d: RICHARD\n"% C)
readfile.close()
putfile.close()
