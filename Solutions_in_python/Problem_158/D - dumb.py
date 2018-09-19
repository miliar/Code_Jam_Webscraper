f = open("d-small.in")
o = open("d-small.out", "w+")

line = f.readline()
T = int(line[:-1])

for rep in range(T):
    line = f.readline()
    L = line[:-1] if line[-1] == '\n' else line
    L = L.split(" ")
    [X, R, C] = [int(i) for i in L]

    #R always > C
    if C > R:
        C, R = R, C
        
    print("X:",X,"RxC:",R,"x",C)
    win = 1
    
    if (R*C)%X != 0:
        win = 0

    #Get all 'biggest' pieces
    biggestArea = []
    for i in range(X):
        if (1+i) > (X-i):
            break
        biggestArea.append([X-i, 1+i])
    
    print(biggestArea)

    #Check all pieces to see if they are bigger than our area
    for bigArea in biggestArea:
        if bigArea[0] > R or bigArea[1] > C:
            win = 0
            break;

    #There is one case: T-block on a 2x4 grid, in which
    #Richard wins. This case was found by extensive search.
    if R==4 and C==2 and X == 4:
        win = 0
        
    if win == 0:
        ans = 'RICHARD'
    else:
        ans = 'GABRIEL'

    
    print("Case #%d: %s\n"%(rep+1, ans))
    o.write("Case #%d: %s\n"%(rep+1, ans))
o.close()
f.close()
