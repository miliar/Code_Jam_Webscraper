inf = open('input.txt', mode='r')
outf = open('output.txt', mode='w')
cases = int(inf.readline())

for case in range(1, cases + 1):
    rstr = "Case #" + str(case) + ": "
    hd, ad, hk, ak, b, d = [int(x) for x in inf.readline().split()]

    def max_dmg(turns):
        if b == 0:
            return turns * ad
        buffs = (ad - turns * b) // (-2 * b)
        return max((buffs * b + ad) * (turns - buffs),
                   ((buffs + 1) * b + ad) * (turns - (buffs + 1)))

    def total(attacks, debuffs):
        res = debuffs + attacks
        hd_cur = hd
        ak_cur = ak
        for i in range(debuffs):
            if hd_cur <= ak_cur - d:
                res += 1
                hd_cur = hd - ak_cur
            ak_cur = max(0, ak_cur - d)
            hd_cur -= ak_cur

        for i in range(attacks - 1):
            if hd_cur <= ak_cur:
                res += 1
                hd_cur = hd - ak_cur
            hd_cur -= ak_cur
            if hd_cur <= 0:
                return 999999999999999

        return res

    mind = 1
    maxd = (hk // ad) + 1
    while mind < maxd:
        mid = (mind + maxd) // 2
        dmg = max_dmg(mid)
        if dmg < hk:
            mind = mid + 1
        else:
            maxd = mid
    attacks = maxd
    if 2 * ak - 3 * d >= hd:
        if attacks > 2:
            rstr += 'IMPOSSIBLE'
        elif attacks == 2 and ak < hd:
            rstr += '2'
        elif attacks == 1:
            rstr += '1'

    else:
        options = []
        for dbfs in range(0, 100):
            options.append(total(attacks, dbfs))

        rstr += str(min(options))
    print(rstr)
    outf.write(rstr + '\n')
