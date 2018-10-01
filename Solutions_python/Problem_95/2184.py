input ="""
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
"""

output = """
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
"""

D = {}
for x, y in zip(list(input), list(output)):
    D[x] = y


def _translate(string, D):
    return "".join([D.get(x, "*") for x in list(string)])


def translate(lines, D):
    i = 1
    L = []
    for line in lines:
        L.append("Case #%d: %s" % (i, _translate(line, D)))
        i+=1
    return "".join(L)

D["z"] = "q"
D["q"] = "z"

def solve(io):
    N = int(io.readline())
    lines = []
    for _ in range(N):
        lines.append(io.readline())
    return translate(lines, D)

    
if __name__ == "__main__":
    import sys
    print solve(sys.stdin)    
