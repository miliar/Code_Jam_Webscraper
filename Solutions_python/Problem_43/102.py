import sys
from collections import defaultdict

output_line = "Case #{X:d}: {V}"



if __name__ == "__main__":
    infile, outfile = sys.argv[1:]
    with open(infile, "r") as inhandle, open(outfile, "w") as outhandle:
        T = int(inhandle.readline())
        for t in range(T):
            msg = inhandle.readline().strip()
            cur = 0
            assignments = {msg[0]:1}
            newmsg = []
            for x in msg:
                if x not in assignments:
                    assignments[x] = cur
                    cur += 1
                    if cur == 1: cur = 2
                newmsg.append(assignments[x])
            base = max(2, cur)

            #print(base, newmsg)

            total = 0
            multiplier = 1
            for x in reversed(newmsg):
                total += x * multiplier
                multiplier *= base

            print(output_line.format(X=t + 1, V=total), file=outhandle)
