from pulp import *
# import time
def main(nbegin, nend):
    for case in range(nbegin, nend + 1):
        # input
#         t0 = time.time()
        n, m = [int(s) for s in input().split(" ")]
        d = {}
        for model in range(0, m):
            kind, i, j = [s for s in input().split(" ")]
            i = int(i)
            j = int(j)
            d[(i,j)] = kind
        # print(d)

        # IP
        vals = [1, 2, 3]
        rows = [i for i in range(1, n+1)]
        cols = [i for i in range(1, n+1)]
        rc = [(r,c) for r in rows for c in cols]

        prob = LpProblem("case", LpMaximize)
        choices = LpVariable.dicts("Choice",(vals,rows,cols),0,1,LpInteger)
        # optimize score
        score = {1:1, 2:1, 3:2}
    #     t1 = time.time()
        prob += lpSum(score[v] * choices[v][r][c] for v in vals for r,c in rc)

    #     t2 = time.time()
        for r, c in rc:
            prob += lpSum([choices[v][r][c] for v in vals]) <= 1, ""#"one in cell {},{}".format(r,c)
    #     t3 = time.time()
        for r in rows:  # r, c
            prob += lpSum([choices[v][r][c] for v in [2, 3] for c in cols]) <= 1, ""# "rows {}".format(r)
        for c in cols:
            prob += lpSum([choices[v][r][c] for v in [2, 3] for r in rows]) <= 1, ""#"cols {}".format(c)

        for diff in range(2-n, n-2+1):
            prob += lpSum([choices[v][r][r-diff] for v in [1,3] for r in range(1, n+1) if (r-diff >=1 and r-diff <= n)]) <= 1, ""
        for diff in range(3, n*2):
            prob += lpSum([choices[v][r][diff-r] for v in [1,3] for r in range(1, n+1) if (diff-r >=1 and diff-r <= n)]) <= 1, ""

        for key in d:  # pre-build models
            r, c = key[0], key[1]
            if d[key] == '+':  # 1
                prob += lpSum([choices[v][r][c]] for v in [1,3]) == 1, ""# "pre, {}{}={}".format(r,c,1)
            elif d[key] == 'x':  # 2
                prob += lpSum([choices[v][r][c]] for v in [2,3]) == 1,  ""#"pre, {}{}={}".format(r,c,2)
            else:  # 3
                prob += lpSum([choices[3][r][c]]) == 1,  ""#"pre, {}{}={}".format(r,c,3)
    #     t4 = time.time()
        prob.solve(GUROBI_CMD(msg=False))
        # prob.solve(PULP_CBC_CMD())

        # print("status:", LpStatus[prob.status])

        y, z = 0, 0
        added = {}
        for r,c in rc:
            for v in vals:
                ans = value(choices[v][r][c])
                if ans != 0:
                    d2 = {1:"+", 2:"x", 3:"o"}
                    if (r,c) not in d:
                        z += 1
                        if v == 3:
                            y += 2
                        else:
                            y += 1
                        added[(r,c)] = d2[v]
                    elif d2[v] != d[(r,c)]:  # sbu
                        z += 1
                        if v == 3:
                            y += 2
                        else:
                            y += 1
                        added[(r,c)] = d2[v]
                    else:
                        if v == 3:
                            y += 2
                        else:
                            y += 1
                        # print(d2[v], y)
        # output
        print("Case #{}: {} {}".format(case, y, z))
        for key in added:
            print("{} {} {}".format(added[key], key[0], key[1]))
 #        t1 = time.time()
        # print(t1-t0)

import sys
script, nbegin, nend = sys.argv
main(int(nbegin), int(nend))
"""
import cProfile
cProfile.run('main()', 'restats')

import pstats
p = pstats.Stats('restats')  # pstats 读取输出的结果
p.sort_stats('cumulative').print_stats(20)  # 按照 cumtime 排序, print_stats(n) 则显示前 n 行
"""
