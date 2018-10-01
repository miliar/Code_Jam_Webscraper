# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())
for i in xrange(1, t + 1):
    n, m = [s for s in raw_input().split(" ")]
    cakes = list(n)
    size = int(m)
    res = 0

    if len(set(cakes)) == 1 and cakes[0] == "+":
        res = 0
    else:
        it = 0
        j = size
        while j <= len(cakes):
            if cakes[it] == "+":
                it += 1
                j += 1
            else:
                for a in range(it, it+size):
                    if it+size <= len(cakes):
                        if cakes[a] == "-":
                            cakes[a] = "+"
                        else:
                            cakes[a] = "-"
                it += 1
                j += 1
                res += 1
        if not (len(set(cakes[it:])) == 1 and cakes[it] == "+"):
            res = "IMPOSSIBLE"
    print "Case #{}: {}".format(i, res)
