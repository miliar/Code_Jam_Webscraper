def build_f(g, k):
    N = len(g)
    L = [0] * N
    for i in range(N):
        tg = g[i:] + g[:i]
        s = 0
        for j in range(N):
            s += tg[j]
            if s > k:
                break
        else:
            s += tg[j]
        L[i] = ((i + j) % N, s - tg[j])
    return L

def find_loop(f, start = 0):
    x = f[start][0]
    y = f[f[start][0]][0]
    
    while x != y:
        x = f[x][0]
        y = f[f[y][0]][0]

    z = f[x][0]
    t = 1
    while z != x:
        z = f[z][0]
        t += 1


    y = start
    s = 0
    while x != y:
        x = f[x][0]
        y = f[y][0]
        s += 1

    return t, s

def find_income(g, k, R):
    f = build_f(g, k)
    t, s = find_loop(f)
    k = (R - s) / t
    q = R - s - k* t
    # s + k * t + q == R
    
    income = 0
    x = 0
    for i in range(s):
        income += f[x][1]
        x = f[x][0]
        
    round_income = 0
    for i in range(t):
        round_income += f[x][1]
        x = f[x][0]
    income += round_income * k
    
    for i in range(q):
        income += f[x][1]
        x = f[x][0]
    return income

def parse_input_and_output(infile, outfile):
    lines = open(infile).readlines()
    RES = []
    for i, (line1, line2) in enumerate(zip(lines[1::2], lines[2::2])):
        try:
            R, k, N = map(int, line1.split())
            g = map(int, line2.split())
            res = find_income(g, k, R)
            RES.append("Case #%d: %s" % (i + 1, res))
        except (IndexError, ValueError):
            pass
    open(outfile, "w").write("\n".join(RES))
