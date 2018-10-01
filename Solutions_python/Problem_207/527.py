def solve(R, O, Y, G, B, V):
    N = sum([R, O, Y, G, B, V])

    def finish(r, y, b):
        colors = {"R":r, "Y":y, "B":b}
        def get(e, colors):
            if e is None:
                return max(colors.keys(), key = lambda x: colors[x])
            else:
                return max((k for k in colors.keys() if k != e), key = lambda x: colors[x])

        q = ""
        flag = True
        while (colors["R"] != colors["Y"] or colors["Y"] != colors["B"] or colors["B"] != colors["R"]) and flag:
            flag = False

            e = get(None, colors) if len(q) == 0 else get(q[-1], colors)
            if colors[e] != 0:
                q += e
                colors[e] -= 1
                flag = True

        if not flag: return "IMPOSSIBLE"

        r = colors["R"]
        if r != 0:
            if len(q) == 0: q = "BRY" * r
            elif q[0] == 'R':
                if q[-1] == 'Y': q += "BRY" * r
                else: q += "YRB" * r
            elif q[0] == 'Y':
                if q[-1] == 'B': q += "RYB" * r
                else: q += "BYR" * r
            elif q[0] == 'B':
                if q[-1] == 'R': q += "YBR" * r
                else: q += "RBY" * r

        if q[0] == q[-1]: return "IMPOSSIBLE"

        return q

    return finish(R, Y, B)

def input(file):
    F = open(file, "r")
    T = int(F.readline())
    for i in range(T):
        N, R, O, Y, G, B, V = F.readline().split(" ")
        yield i + 1, int(R), int(O), int(Y), int(G), int(B), int(V)

out = open("B.out", "w")

#for (i, R, O, Y, G, B, V) in input("Bsample.in"):
for (i, R, O, Y, G, B, V) in input("B-small-attempt0.in"):
#for (i, R, O, Y, G, B, V) in input("B-large.in"):
    w = "Case #%d: %s" % (i, solve(R, O, Y, G, B, V))
    print(w)
    print(w, file = out)
