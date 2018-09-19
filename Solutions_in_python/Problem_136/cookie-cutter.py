o = open('output.txt', 'w')

with open('input.txt', 'r') as f:
    lines = f.readlines()

n = int(lines[0])

for i in range(1, n+1):
    line = lines[i].strip().split()

    r = 2
    c = float(line[0])
    f = float(line[1])
    x = float(line[2])

    ans = x/r
    maxF = int(x/c)

    for xf in range(maxF + 1):
        a1 = 0
        r1 = r
        for j in range(xf):
            a1 = a1 + c/r1
            r1 = r1 + f
        a1 = a1 + x/r1

        ans = min(ans, a1)

    o.write('Case #%s: %s\n' % (i, "{0:.7f}".format(ans)))

o.close()
