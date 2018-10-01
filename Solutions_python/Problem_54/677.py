import functools

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


src = open("B-large.in", "r")
out = open("B-large-results.in", "w")

c = int(src.readline())

for i in range(1, c + 1):
    tt = list(map(int, src.readline().split()))
    n = tt[0]
    del tt[0]

    a = min(tt)
    topt = functools.reduce(gcd, [t - a for t in tt])
    y = -a % topt
    ans = "Case #{0}: {1}".format(i, y)
    if i != c:
        ans += '\n'

    out.write(ans)

out.close()

    
