import sys
sys.stdout = open("out.txt", "w")


def solve(r, o, y, g, b, v):
    ans = "IMPOSSIBLE"
    if r+y >=b and y+b>=r and b+r>=y:
        cnt = {'R':r,'Y':y,'B':b}
        icnt = sorted({'R': r, 'Y': y, 'B': b}, key=lambda x: cnt[x], reverse=True)
        ans=""
        prev = ""
        while cnt['R']>0 or cnt['Y']>0 or cnt['B']>0:
            k = max(icnt, key=(lambda key: cnt[key] if key!=prev else 0))
            ans += k
            cnt[k] -= 1
            prev = k
    return ans


lines = []

with open("B-small-attempt0.in", "r") as f:
    lines = f.readlines()

t = int(lines[0])
ctr = 1
for i in range(1, t+1):
    n, r, o, y, g, b, v = lines[i].split()
    n = int(n)
    r = int(r)
    o = int(o)
    y = int(y)
    g = int(g)
    b = int(b)
    v = int(v)
    ans = solve(r, o, y, g, b, v)
    print("Case #{}: {}".format(i, str(ans)))
