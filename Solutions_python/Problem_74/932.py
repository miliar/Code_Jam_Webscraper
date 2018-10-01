from sys import stdin

def riadok():
    return stdin.readline().split()

for cas in range(int(stdin.readline())):
    a = [0, 0]
    pos = [1, 1]
    b = riadok()[1:]
    for i in range(0, len(b), 2):
        u, t = 0, int(b[i + 1])
        if b[i] == 'O':
            u = 1
        a[u] += abs(pos[u] - t)
        a[u], pos[u] = max(a) + 1, t
    print "Case #%d: %d" % (cas + 1, max(a))
