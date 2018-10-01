T = int(input())
for case in range(T):
    line = input()
    D = int(line.split(" ")[0])
    N = int(line.split(" ")[1])
    gT = 0
    for horse in range(N):
        line = input()
        K = int(line.split(" ")[0])
        S = int(line.split(" ")[1])
        T = (D - K)/S
        if (gT < T):
            gT = T

    print("Case #{}: {}".format(case+1, D/gT))


