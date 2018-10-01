import os
import os.path

def solve(candy):
    candy.sort()
    if reduce(lambda x, y: x^y, candy) == 0:
        return str(sum(candy[1:]))
    else:
        return "NO"

def candy(path):
    fin = open(path)
    out_path = os.path.splitext(path)[0] + ".sol"
    fout = open(out_path, "w")

    num_cases = int(fin.readline().strip())

    for i in range(num_cases):
        num_candy = int(fin.readline().strip())
        candy = fin.readline().strip().split()
        candy = [int(c) for c in candy]
        sol = solve(candy)
        fout.write("Case #%i: %s\n" % (i+1, sol))

    fout.close()
    fin.close()
