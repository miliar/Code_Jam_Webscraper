def findWinner(ls):
    dia1 = ""
    for i in range(0, 4):
        dia1 += ls[i][i]
    dia2 = ""
    for i in range(0,4):
        dia2 += ls[i][3-i]
    cols = []
    for i in range(0, 4):
        t = ""
        for k in range(0, 4):
            t += ls[k][i]
        cols.append(t)
    ls.append(dia1)
    ls.append(dia2)
    ls += cols
    winSet = False
    dfound = False
    rply = "Draw"
    for s in ls:
        if "." in s:
            dfound = True
            continue
        elif "X" not in s:
            winSet = True
            rply = "O won"
        elif "O" not in s:
            winSet = True
            rply = "X won"
    if not winSet and dfound:
        rply = "Game has not completed"
    return rply
        
        
T = int(input())
for i in range(0, T):
    table = []
    for j in range(0, 4):
        r = str()
        r = raw_input()
        table.append(r)
    print "Case #" + str(i+1) +": " + findWinner(table)
    if i != T-1:
        empty = raw_input()
    
        
