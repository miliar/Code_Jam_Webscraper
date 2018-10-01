from math import ceil

filein = open('B-large.in.txt', 'r')
fileout = open('B-large.out.txt', 'w')
T = int(filein.readline())
for t in range(T):
        ## dealing with data

    fileout.write('Case #%d: ' % (t + 1))
    inp = [int(x) for x in  filein.readline().split()]
    N, P = inp[0], inp[1]
    Q = [int(x) for x in filein.readline().split()]
    l = [[] for x in range(N)]
    for i in range(N):
        weights = [int(x) for x in filein.readline().split()]
        for j in range(P):
            lb = max(1, int(ceil(weights[j]/1.1/Q[i])))
            ub = int(weights[j]/0.9/Q[i])
            if ub >= 1 and ub * Q[i] * 1.1 >= weights[j]:
                l[i].append([lb, ub])

        l[i].sort(key=lambda x: x[1])
        l[i].sort(key=lambda x: x[0])
    ans = 0
    ## typical interview question
    while all(x for x in l):
        [s, e] = l[0][0]
        temp = [(x[0], n) for n, x in enumerate(l)]
        mx = max(temp)[0][0]
        mn = min(temp)[0][1]
        if mx <= mn:
            ans += 1
            for i in range(len(l)):
                del l[i][0]
        else:
            for n in (x[1] for x in temp if x[0][0] <= mn):
                del l[n][0]
    fileout.write(str(ans) + '\n')

filein.close()
fileout.close()