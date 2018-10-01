'''
Created on May 30, 2015

@author: billyanhuang
'''
def checkDir(pos, i, j, R, C):
    dirs = set([])
    t = i
    while (t < R-1):
        t += 1
        if pos[t][j] != ".":
            dirs.add("v")
            break
    t = i
    while (t > 0):
        t -= 1
        if pos[t][j] != ".":
            dirs.add("^")
            break
    t = j
    while (t < C-1):
        t += 1
        if pos[i][t] != ".":
            dirs.add(">")
            break
    t = j
    while (t > 0):
        t -= 1
        if pos[i][t] != ".":
            dirs.add("<")
            break
    return dirs

filename = 'A-large.'

fin = open(filename + 'in', 'r')
fout = open(filename + 'out', 'w')

T = int(fin.readline())
for t in range(T):
    inp = fin.readline().split()
    R = int(inp[0])
    C = int(inp[1])
    #initiating
    pos = []
    for i in range(R):
        row = []
        inp = fin.readline().replace("\n", "")
        row.extend(inp)
        pos.append(row)
    #counting values
    num = 0
    possible = True
    for i in range(R):
        for j in range(C):
            if pos[i][j] != ".":
                dirs = checkDir(pos, i, j, R, C)
                if len(dirs) == 0:
                    possible = False
                if pos[i][j] not in dirs:
                    num += 1
    if not possible:
        num = "IMPOSSIBLE"
    fout.write("Case #" + str(t+1) + ": " + str(num) + "\n")