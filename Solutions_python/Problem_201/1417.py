from math import ceil

TEST = False

def read(file):
    if TEST:
        return input()
    return file.readline()

def write(s, file):
    if TEST:
        print(s)
    else:
        print(s, file=file)

rfile, wfile = None, None
if not TEST:
    fname = input().strip()

    rfile = open(''.join([fname, '.in']), 'r')
    wfile = open(''.join([fname,'.out']), 'w')

T = int(read(rfile))
for i in range(1, T + 1):
    n, k = [int(e) for e in read(rfile).split()]
    d = {n:1}
    a, b = 0, 0
    for j in range(k):
        m = max(d)
        if d[m] == 1:
            del d[m]
        else:
            d[m] -= 1
        m -= 1
        b = m//2
        a = ceil(m/2)
        d[a] = d.get(a, 0)+1
        d[b] = d.get(b, 0)+1
    write("Case #{}: {} {}".format(i, max(a,b), min(a,b)), file=wfile)

if not TEST:
    rfile.close()
    wfile.close()
