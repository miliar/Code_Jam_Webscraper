import sys

args = sys.argv

if len(args) < 2:
    print 'small or large?'
    exit()

inp = args[1]

out = open(inp + '_OUT', 'w')

# No change before this

def int_row():
    return map(int, raw_input().split())

def solve():
    n, m = int_row()
    rows = []
    cols = []
    rmax = []
    for i in xrange(m):
        cols.append([])
    for i in xrange(n):
        r = int_row()
        rmax.append(max(r))
        rows.append(r)
        for j in xrange(m):
            cols[j].append(r[j])
    cmax = []
    for c in cols:
        cmax.append(max(c))
    for i in xrange(n):
        for j in xrange(m):
            t = rows[i][j]
            if t < cmax[j] and t < rmax[i]:
                return 'NO'
    return 'YES'

T = input()
for i in xrange(1, T+1):
    ans = 'Case #' + str(i) + ': ' + solve()
    print ans
    out.write(ans + '\n')

# No change after this

out.close()
