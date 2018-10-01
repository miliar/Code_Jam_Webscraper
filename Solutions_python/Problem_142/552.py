t = int(input())

def solve(s):
    todasletras = set()
    rs = []
    for c in s:
        for l in c:
            todasletras.add(l)

    for c in s:
        rc = []
        for l in c:
            if not l in todasletras:
                return "Fegla Won"

            if rc == [] or l != rc[-1][0]:
                rc += [[l, 0]]

            if l == rc[-1][0]:
                rc[-1][1] += 1
        rs += [rc]
    fs = set()

    for s in rs:
        f = ""
        for c in s:
            f += c[0]
        fs.add(f)

    if len(fs) > 1:
        return "Fegla Won"

    iis = []
    for s in rs:
        i = []
        for c in s:
            i.append(c[1])
        iis.append(tuple(i))

    if iis[0] == iis[1]:
        return 0
    ops = 0

    for i0, i1 in zip(iis[0], iis[1]):
        ops += abs(i0-i1)

    return ops

for case in range(t):
    n = int(input())
    s = []
    for _ in range(n):
        s += [input()]

    print ("Case #%s: %s" % (case+1, solve(s)))
