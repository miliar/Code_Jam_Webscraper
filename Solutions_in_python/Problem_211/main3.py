import numpy as np

def solve(n, k, u, probabilita):
    assert n == k, (n, k)
    # somma_prob = sum(probabilita)
    # rimasto = 1.0 * n - somma_prob
    # limite = 1.0 - (rimasto - u) / n
    # new_prob = [p if p >= limite else limite for p in probabilita]
    new_prob = probabilita[:] + [1.1]
    ru = u
    while ru > 0:
        # print new_prob
        min_p = min(new_prob)
        # print min_p
        second_min_p = min(p for p in new_prob if abs(p - min_p) > 10 ** -8)
        n_min = len([p for p in new_prob if abs(p - min_p) < 10 ** -8])
        min_diff = min(second_min_p - min_p, ru)
        ru -= min_diff
        each_u = min_diff / n_min
        new_prob = [p if abs(p - min_p) > 10 ** -8 else (p + each_u) for p in new_prob]
        # if abs(sum(new_prob)- (n+1)) < 10 ** -8:
        #     break

    prod = 1
    for p in new_prob:
        if p < 1.05:
            prod *= p
    return prod


risultati = []
with open("C-small-1-attempt0.in") as f:
    t = int(f.readline())
    print "t", t
    for i in range(t):
        row = f.readline().strip()
        nr, kr = [int(c) for c in row.split(" ")]
        print nr, kr
        row = f.readline().strip()
        ur = float(row)
        print ur
        row = f.readline().strip()
        prob = [float(c) for c in row.split(" ")]
        print prob
        if nr == kr:
            s = solve(n=nr, k=kr, u=ur, probabilita=prob)
            print "solve: {}".format(s)
            risultati.append(s)


with open("outCSmall0.txt", "w") as out:
    for i, r in enumerate(risultati):
        out.write("Case #{}: {:.6f}\n".format(i+1, r))
