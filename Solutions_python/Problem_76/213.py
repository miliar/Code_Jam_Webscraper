import operator

def is_possible(L):
    if reduce(operator.xor, L) == 0:
        return True
    return False

def solve_C(infile, outfile):
    inputs = open(infile).readlines()[2::2]
    R = []
    for i, inp in enumerate(inputs):
        candy_vals = map(int, inp.split())
        if is_possible(candy_vals):
            res = str(sum(candy_vals) - min(candy_vals))
        else:
            res = "NO"
        R.append("Case #%d: %s" % (i + 1, res))
    open(outfile, "w").write("\n".join(R))

