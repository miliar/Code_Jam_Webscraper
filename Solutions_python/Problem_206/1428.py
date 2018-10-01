import fileinput


def solve(d, n, k, s):
    sol = 0.0
    for i in range(0, n):
        m = (d - k[i])/s[i]
        if m > sol:
            sol = m

    sol = d / sol
    return sol

reader = fileinput.input()
t = int(reader.readline())
for i in range(1, t+1):
    d, n = [int(r) for r in reader.readline().strip().split(" ")]
    k = []
    s = []
    for x in range(0, n):
        rk, rs = [int(r) for r in reader.readline().strip().split(" ")]
        k.append(rk)
        s.append(rs)
    print("Case #{}: {}".format(i, solve(d, n, k, s)))

