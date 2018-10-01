f = open("candy.large.in", "r")

t = int(f.readline())

N = []
C = []

for i in range(0, t):
    n = int(f.readline())
    N.append(n)

    C.append([])
    v = f.readline().split(" ")
    for j in range(0, n):
        C[i].append(int(v[j]))


f.close()


f = open("candy.out", "w")

for u in range(0, t):
    xorsum = 0
    
    for i in range(0, N[u]):
        xorsum ^= C[u][i]

    if (xorsum == 0):
        f.write("Case #" + str(u + 1) + ": " + str(sum(C[u]) - min(C[u])) + "\n")
    else:
        f.write("Case #" + str(u + 1) + ": NO\n")
        
f.close()

print "done"
