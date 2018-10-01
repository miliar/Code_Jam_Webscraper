def num(s, c, t=None):
    res = 0
    for sc in s:
        if sc == c:
            res += 1
        if sc == t:
            res += 1
    return res

inf = open("a.in", "r")
ouf = open("a.out", "w")
T = int(inf.readline())
N = 4
a = ["." * N] * N
for t in range(T):
    print("Case #", (t + 1), ": ", sep="", end="", file=ouf)
    for i in range(N):
        a[i] = inf.readline().strip()
    inf.readline()
    candidates = [a[i] for i in range(N)] + \
                 ["".join(a[i][j] for i in range(N)) for j in range(N)] + \
                 ["".join(a[i][i] for i in range(N))] + ["".join(a[i][N - i - 1] for i in range(N))]
    if any(num(c, "X", "T") == 4 for c in candidates):
        print("X won", file=ouf)
    elif any(num(c, "O", "T") == 4 for c in candidates):
        print("O won", file=ouf)
    elif any(num(c, ".") > 0 for c in candidates):
        print("Game has not completed", file=ouf)
    else:
        print("Draw", file=ouf)
inf.close()
ouf.close()    

