import sys
T = int(raw_input())
for Ti in range(1,T+1):
    s = [int(m) for m in raw_input().split()]
    N = s[0]
    s = s[1:]
    X = sum(s)
    sys.stdout.write("Case #%d: " % (Ti))
    for i in range(len(s)):
        t = sorted(s[:i] + s[i+1:])
        su = 0
        best = 100.0
        for j in range(len(t)):
            su += t[j]
            y = float(su - (j+1)*s[i] + X) / ((j+2)*X)
            if y < best:
                best = y
        if best < 0.0:
            best = 0.0
        sys.stdout.write("%f " %(100*best))
    print ""
