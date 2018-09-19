def disttris(tups):
    count = 0
    while len(tups) > 2:
        curt = tups[0]
        ttups = tups[1:]
        while len(ttups) > 1:
            for x in ttups[1:]:
                if (curt[0] + ttups[0][0] + x[0])%3 == 0:
                    if (curt[1] + ttups[0][1] + x[1])%3 == 0:
                        print curt, ttups[0], x
                        count+=1
            ttups = ttups[1:]
        tups = tups[1:]
    return str(count)
def treetups(input):
    n, A, B, C, D, x0, y0, M = input
    X = x0
    Y = y0
    tups = [(X, Y)]
    for i in range(1,n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        tups.append((X,Y))
    return tups
try:
    f = open("input/A-small.in")
    fout = open("input/A-small.out",'w')
    for case in range(int(f.readline())):
        input = map(int,f.readline().split())
        tups = treetups(input)
        fout.write("Case #" + str(case + 1) + ": " + disttris(tups) + "\n")
    f.close()
    fout.close()
except:
    f.close()
    fout.close()