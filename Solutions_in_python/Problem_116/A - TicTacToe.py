def game():
    f = open("A-large0.in", "r")
    output = open("A-large.out", "w")
    first = f.readline()
    T = int(first)
    case = 1

    while case < T+1:
        grid = [[],[],[],[]]
        for i in range(4):
            line = f.readline()
            line1 = list(line)
            grid[i] = line1[:-1]
        #print grid
        res = "Case #" + str(case) + ": "+ result(grid)+"\n"
        #print res
        output.write(res)
        case = case+1
        f.readline()
    f.close()
    

def result(grid):

    #Line check
    for i in range(4):
        if(grid[i].count("T")+grid[i].count("X") == 4):
            return "X won"
        if(grid[i].count("T")+grid[i].count("O") == 4):
            return "O won"

    #Column check
    for i in range(4):
        if((grid[0][i]+grid[1][i]+grid[2][i]+grid[3][i]).count("X")+
(grid[0][i]+grid[1][i]+grid[2][i]+grid[3][i]).count("T") == 4):
            return "X won"
        if((grid[0][i]+grid[1][i]+grid[2][i]+grid[3][i]).count("O")+
(grid[0][i]+grid[1][i]+grid[2][i]+grid[3][i]).count("T") == 4):
            return "O won"

    #Diagonal Check
    if((grid[0][0]+grid[1][1]+grid[2][2]+grid[3][3]).count("X")+
(grid[0][0]+grid[1][1]+grid[2][2]+grid[3][3]).count("T") == 4):
            return "X won"
    if((grid[0][0]+grid[1][1]+grid[2][2]+grid[3][3]).count("O")+
(grid[0][0]+grid[1][1]+grid[2][2]+grid[3][3]).count("T") == 4):
            return "O won"
    if((grid[3][0]+grid[2][1]+grid[1][2]+grid[0][3]).count("X")+
(grid[3][0]+grid[2][1]+grid[1][2]+grid[0][3]).count("T") == 4):
            return "X won"
    if((grid[3][0]+grid[2][1]+grid[1][2]+grid[0][3]).count("O")+
(grid[3][0]+grid[2][1]+grid[1][2]+grid[0][3]).count("T") == 4):
            return "O won"

    #No Solution?
    for i in grid:
        if i.count(".")>0:
            return "Game has not completed"

    return "Draw"

game()
