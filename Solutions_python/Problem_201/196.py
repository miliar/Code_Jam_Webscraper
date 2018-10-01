def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z

def gen_add_table(num):
    seen = set()
    def pgen_add_table(seed):
        if seed < 1 or seed in seen:
            return {}
        seen.add(seed)
        parity = seed % 2
        d = {seed: [seed//2 - int(not(parity)), 1, seed//2]}
        ds = reduce(merge_two_dicts, map(pgen_add_table, d[seed]), {})
        return merge_two_dicts(d, ds)
    return pgen_add_table(num)

def appearances(seed, gat):
    d = {seed: 1}
    sgats = sorted(gat.items(), reverse=True)
    for i in xrange(len(sgats)):
        for j in reversed(xrange(i)):
            d[sgats[i][0]] = d.get(sgats[i][0], 0) + d[sgats[j][0]] * sgats[j][~0].count(sgats[i][0])
    return d

def getit(seed):
    gat = gen_add_table(seed)
    return sorted(appearances(seed, gat).items(), reverse=True), gat

t = int(raw_input())
for x in xrange(t):
    n, k = tuple(map(int, raw_input().split()))
    ap, gat = getit(n)
    i = 0
    while True:
        if ap[i][~0] >= k or ap[i][~0] is None:
            print 'Case #{}: {} {}'.format(
                x+1, gat[ap[i][0]][~0], gat[ap[i][0]][0]
            )
            break
        else:
            k -= ap[i][~0]
            i += 1
