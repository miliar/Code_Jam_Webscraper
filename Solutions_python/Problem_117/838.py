def through(table, n, m, i, j):
    height = table[i][j]
    for t in range(0, n):
        if table[t][j] > height:
            for p in range(0, m):
                if table[i][p] > height:
                    return [-1, -1]
            return [1, -1]
    return [-1, 1]

def lawnmower(table, n, m):
    resultRow = [-1 for row in range(N)]
    resultCol = [-1 for col in range(M)]
    for i in range(0, n):
        for j in range(0, m):
            if resultRow[i] > 0 or resultCol[j] > 0:
                continue
            t = through(table, n, m, i, j)
            row = t[0]
            col = t[1]
            if resultRow[i] < row:
                resultRow[i] == 1
            if resultCol[j] < col:
                resultCol[j] == 1
            if row < 0 and col < 0:
                return "NO"
            else:
                continue
    return "YES"


f = open("B-large.in", "r")
out = open("B-large.out", "w")
line = f.readline()
T = int(line)
for i in range(0, T):
    line = f.readline()
    line = line.split(" ")
    N = int(line[0])
    M = int(line[1])
    matrix = [[0 for col in range(M)] for row in range(N)]
    for j in range(0, N):
        line = f.readline()
        line = line.split(" ")
        for k in range(0, M):
            matrix[j][k] = int(line[k])
        result = lawnmower(matrix, N, M)
#    print "Case #%d: %s" %(i+1, result)
    out.write("Case #%d: %s\n" %(i+1, result))
f.close()
out.close()
