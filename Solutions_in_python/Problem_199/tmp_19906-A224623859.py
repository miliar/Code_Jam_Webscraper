import sys

sys.stdin.readline()

for (cn, ln) in enumerate(sys.stdin.readlines(), 1):
    fl = int(ln.split(' ')[1])
    pnc = [True] + list(map(lambda c: c == '+', ln.split(' ')[0]))
    pnc = list(map(lambda a: a[0] ^ a[1], zip(pnc, pnc[1:]))) + [False]
    n = 0
    for i in range(len(pnc)-fl):
        if pnc[i]:
            n = n + 1
            pnc[i] = not pnc[i]
            pnc[i+fl] = not pnc[i+fl]
    if any(pnc[:-1]): n = 'IMPOSSIBLE'
    print('Case #%s: %s' % (cn, n))
