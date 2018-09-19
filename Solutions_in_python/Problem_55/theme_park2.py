import sys, itertools
from collections import namedtuple
from itertools import chain, cycle
from pprint import pprint

output_line = "Case #{X:d}: {profit:d}"

DPData = namedtuple("DPData", "next_i profit")

DPCycle = namedtuple("DPCycle", "last_r last_profit")

if __name__ == "__main__":
    infile, outfile = sys.argv[1:]
    with open(infile, "r") as inhandle, open(outfile, "w") as outhandle:
        T = int(inhandle.readline())
        for t in range(T):
            R, k, N = map(int, inhandle.readline().split())
            g = list(map(int, inhandle.readline().split()))

            dp = [None] * N
            dp2 = [None] * N

            total = 0
            i = 0 #line position

            r = 0
            while r < R: #for reach rollercoaster run
                if dp2 and dp2[i]:
                    profitcycle = total - dp2[i].last_profit
                    rcycle = r - dp2[i].last_r

                    cycleleft = (R - r) // rcycle
                    total += cycleleft * profitcycle
                    r += cycleleft * rcycle
                    dp2 = None
                    continue
                else:
                    if not dp[i]:
                        peopleon = 0
                        for line_i in chain(range(i, N), range(0, i)):
                            if peopleon + g[line_i] > k:
                                break
                            else:
                                peopleon += g[line_i]
                        dp[i] = DPData(next_i=line_i, profit=peopleon)
                    if dp2: dp2[i] = DPCycle(last_r=r, last_profit=total)
                    total += dp[i].profit
                    i = dp[i].next_i
                r += 1

            #pprint(dp)

            print(output_line.format(X=t + 1, profit=total), file=outhandle)
            print(output_line.format(X=t + 1, profit=total))
