def ed(a, b):
    dist = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i in range(1, len(b)+1):
            dist[0][i] = None
    for i in range(1, len(a)+1):
            dist[i][0] = None
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            rl = []
            if a[i-1] == b[j-1]:
                if dist[i-1][j-1] != None:
                    rl.append(dist[i-1][j-1])
            if j > 1 and b[j-1] == b[j-2]:
                if dist[i][j-1] != None:
                    rl.append(dist[i][j-1]+1)
            if i > 1 and a[i-1] == a[i-2]:
                if dist[i-1][j] != None:
                    rl.append(dist[i-1][j]+1)
            if len(rl) == 0:
                dist[i][j] = None
            else:
                dist[i][j] = min(rl)
    return dist[len(a)][len(b)]



with open('A-small-attempt5.in') as f:
    data = [line.rstrip() for line in f]
i = 1
ncase = 1
while i < len(data):
    print "Case #%d:" % ncase,
    ns = int(data[i])
    ss = data[i+1:i+ns+1]
    i = i + ns + 1
    if len(ss) == 2:
        x = ed(ss[0], ss[1])
        if x == None:
            print "Fegla Won"
        else:
            print x
    else:
        for m in range(1, len(ss)):
            for n in range(m):
                print m, n
                print ed(ss[m], ss[n])
    ncase += 1
