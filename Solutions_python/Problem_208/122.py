import math

inputfilename = "C-large.in"
fin = open(inputfilename, "r")
outputfilename = "pony_express_output.txt"
fout = open(outputfilename, "w")
t = fin.readline()
t = int(t)
for ii in xrange(1, t+1):
    line = fin.readline().split(" ")
    n = int(line[0])
    q = int(line[1])
    enduration = []
    speed = []
    d = []
    time = [[0 for i in xrange(n)] for j in xrange(n)]
    for j in xrange(n):
        line = fin.readline().split(" ")
        enduration.append(int(line[0]))
        speed.append(int(line[1]))
    for j in xrange(n):
        line = fin.readline().split(" ")
        temp = []
        for k in line:
            temp.append(int(k))
        d.append(temp)
    pairs = []
    for j in xrange(q):
        line = fin.readline().split(" ")
        pairs.append((int(line[0]), int(line[1])))
    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                if i == j or i == k or j == k:
                    continue
                if d[i][k] == -1 or d[k][j] == -1:
                    continue
                if d[i][j] == -1:
                    d[i][j] = d[i][k] + d[k][j]
                else:
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    for i in xrange(n):
        for j in xrange(n):
            if d[i][j] == -1 or d[i][j] > enduration[i]:
                time[i][j] = -1
                continue
            time[i][j] = d[i][j] * 1.0 / speed[i]
    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                if i == j or i == k or j == k:
                    continue
                if time[i][k] == -1 or time[k][j] == -1:
                    continue
                if time[i][j] == -1:
                    time[i][j] = time[i][k] + time[k][j]
                else:
                    time[i][j] = min(time[i][j], time[i][k] + time[k][j])

    #result = "Case #" + str(ii) + ": " + deliver(pairs) + '\n'
    result = "Case #" + str(ii) + ": "
    for p in pairs:
        result += " " + str(time[p[0] - 1][p[1] - 1])
    result += '\n'
    fout.write(result)

fin.close()
fout.close()
