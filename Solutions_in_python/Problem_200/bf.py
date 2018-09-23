import sys
for t, line in enumerate(sys.stdin,start=0):
    if t == 0:
        continue
    n = int(line.strip())
    for p in range(n, 0, -1):
        v = str(p)
        if all(v[i] <= v[i+1] for i in range(len(v)-1)):
            print("Case #{}: {}".format(t, v))
            break
