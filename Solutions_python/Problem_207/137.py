IMPOSSIBLE = "IMPOSSIBLE"


def solve_primari(xb, xy, xr):
    supp_list = [(xb, "B"), (xy, "Y"), (xr, "R")]
    supp_list.sort(key=lambda x: -x[0])
    print supp_list
    mstring0 = supp_list[0][1] * supp_list[0][0]
    mstring1 = supp_list[1][1] * supp_list[1][0] + " " * (supp_list[0][0] - supp_list[1][0])
    # mstring2 = supp_list[2][1] * supp_list[2][0] + "" * (supp_list[0][0] - supp_list[2][0])
    part_str = ""
    for m0, m1 in zip(mstring0, mstring1):
        part_str += m0
        part_str += m1 if m1 != " " else ""
    print part_str
    min_res = supp_list[2][0]
    min_c = supp_list[2][1]
    mlen = len(part_str)
    fstr = ""
    for ib in range(mlen):
        ia = (ib + 1) % mlen
        if part_str[ib] != part_str[ia]:
            fstr += part_str[ib]
        else:
            if min_res > 0:
                fstr += part_str[ib]
                fstr +=  min_c
                min_res -= 1
            else:
                return (False, IMPOSSIBLE)
    if min_res == 0:
        print 'fstr', fstr
        return (True, fstr)
    else:
        nfstr = ""
        flen = len(fstr)
        for ib in range(flen):
            ia = (ib + 1) % flen
            nfstr += fstr[ib]
            if min_res > 0 and fstr[ia] != min_c and fstr[ib] != min_c:
                nfstr += min_c
                min_res -= 1

    assert min_res == 0, (min_res, nfstr)
    print 'nfstr', nfstr
    return (True, nfstr)


def solve_singola(c_primario, c_secondario, n_primario, n_secondario):
    if n_primario == n_secondario:
        return (True, (c_primario + c_secondario) * n_secondario)
    else:
        return (False, IMPOSSIBLE)


def crea_catena(c_primario, c_secondario, n_secondario):
    return (c_primario + c_secondario) * n_secondario + c_primario

def sostituisci_catena(mstr, catena, c_catena):
    # print 'mstr', mstr
    nstr = ""
    trovato = False
    for c in mstr:
        if not trovato and c == c_catena:
            nstr += catena
            trovato = True
        else:
            nstr += c
    assert trovato, (mstr, catena)
    # print 'nstr', nstr
    return nstr


def solve(mrow):
    num = [int(x) for x in mrow.split(" ")]
    assert len(num) == 7, (mrow, num)
    n = num[0]
    r, o, y, g, b, v = num[1:]
    if o > 0 or g > 0 or v > 0:
        # caso singola
        if all(x > 0 for x in [y, v]) and all(x == 0 for x in [r, g, b, o]):
            return solve_singola(c_primario="Y", c_secondario="V", n_primario=y, n_secondario=v)[1]
        elif all(x > 0 for x in [r, g]) and all(x == 0 for x in [y, v, b, o]):
            return solve_singola(c_primario="R", c_secondario="G", n_primario=r, n_secondario=g)[1]
        elif all(x > 0 for x in [b, o]) and all(x == 0 for x in [y, v, r, g]):
            return solve_singola(c_primario="B", c_secondario="O", n_primario=b, n_secondario=o)[1]

        # creazioni catene
        catena_v = False
        catena_g = False
        catena_o = False

        if v > 0:
            if v <= y - 1:
                catena_v = True
                y -= v  # + 1
                assert y >= 1, (y, v)
                # v = 0
            else:
                return IMPOSSIBLE
        if o > 0:
            if o <= b - 1:
                catena_o = True
                b -= o  # + 1
                assert b >= 1, (b, o)
                # o = 0
            else:
                return IMPOSSIBLE
        if g > 0:
            if g <= r - 1:
                catena_g = True
                r -= g  # + 1
                assert r >= 1, (r, g)
                # g = 0
            else:
                return IMPOSSIBLE
        res = solve_primari(xb=b, xy=y, xr=r)
        if res[0] == False:
            return IMPOSSIBLE
        basic_str = res[1]
        if catena_v:
            str_catena_v = crea_catena(c_primario="Y", c_secondario="V", n_secondario=v)
            basic_str = sostituisci_catena(mstr=basic_str, catena=str_catena_v, c_catena="Y")
        if catena_o:
            str_catena_o = crea_catena(c_primario="B", c_secondario="O", n_secondario=o)
            basic_str = sostituisci_catena(mstr=basic_str, catena=str_catena_o, c_catena="B")
        if catena_g:
            str_catena_g = crea_catena(c_primario="R", c_secondario="G", n_secondario=g)
            basic_str = sostituisci_catena(mstr=basic_str, catena=str_catena_g, c_catena="R")
        return basic_str
    else:
        possible, res = solve_primari(xb=b, xy=y, xr=r)
        if possible:
            return res
        else:
            return IMPOSSIBLE


risultati = []
with open("B-large.in") as f:
    t = int(f.readline())
    print "t", t
    for i in range(t):
        # n = int(f.readline())
        # print "n", n, i
        row = f.readline().strip()
        print row
        sol = solve(row)
        # print "sol", sol
        assert sol == IMPOSSIBLE or len(sol) == int(row.split(" ")[0]), sol
        risultati.append(solve(row))
# print "risultati\n", risultati
with open("out2Large.txt", "w") as out:
    for i, r in enumerate(risultati):
        out.write("Case #{}: {}\n".format(i+1, r))
