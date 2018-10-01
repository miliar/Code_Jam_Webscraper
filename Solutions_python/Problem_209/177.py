import math

def solve(N, K, rl, hl):
    if K == 0:
        return 0.0
    bestArea = 0
    for bottom in range(0, N):
        r = rl[bottom]
        h = hl[bottom]
        area = r*r + 2*r*h
        al = []
        for i in range(0,N):
            if i == bottom:
                continue
            r = rl[i]
            h = hl[i]
            a = 2*r*h
            al.append(a)
        al.sort(reverse=True)
        for i in range(0,K-1):
            area += al[i]
        bestArea = max(area, bestArea)
    return bestArea
            

with open("A-large.in", "r") as ifile, open("out.txt", "w") as ofile:
    lines = ifile.readlines()
    T = int(lines[0])
    li = 1
    for i in range(0, T):
        [N,K] = map(int,lines[li].split(" "))
        li+=1
        rl = []
        hl = []
        for j in range(0, N):
            [R,H] = map(int,lines[li].split(" "))
            rl.append(R)
            hl.append(H)
            li+=1
        ofile.write("Case #{}: {}\n".format(i+1, math.pi * solve(N, K, rl, hl)))
        