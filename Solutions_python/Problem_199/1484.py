f = open("input.txt")
out = open("output.txt", "w")
t = int(f.readline().strip())
tt = 1
while tt <= t:
    panLine, k = f.readline().strip().split()
    i = res = 0
    k = int(k)
    panLine = list(panLine)
    while (i + k - 1) < len(panLine):
        print panLine, panLine[i], i
        if panLine[i] == "-":
            res += 1
            for j in range(i, i + k):
                if panLine[j] == '-':
                    panLine[j] = '+'
                else:
                    panLine[j] = '-'
        i += 1
    if all(i == '+' for i in panLine[i:]):
        out.write("Case #" + str(tt) + ": " + str(res)+"\n")
    else:
        out.write("Case #" + str(tt) + ": IMPOSSIBLE\n")
    tt += 1
