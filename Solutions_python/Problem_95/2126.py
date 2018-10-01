import sys

def solve(l, casen):
    e="abcdefghijklmnopqrstuvwxyz"
    g="ynficwlbkuomxsevzpdrjgthaq"
    cleartext = ''.join(map(lambda c: e[g.index(c)] if (c in e) else c, list(l)))
    print("Case #%d: %s" % (casen, cleartext))

if __name__ == '__main__':
    with open(sys.argv[1], 'rU') as f:
        lines = f.readlines()
        ncases = int(lines[0])
        lines = lines[1:]
        for i in range(ncases):
            solve(lines[i].strip(), i+1)

