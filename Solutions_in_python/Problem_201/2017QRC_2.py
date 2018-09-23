from math import floor, log2
from collections import defaultdict

with open("C-small-2-attempt1.in", "r") as inp:
    with open("C-small-2-attempt1.out", "w") as outp:
        cases = int(inp.readline().strip())
        for i in range(cases):
            stalls, people = [int(k) for k in inp.readline().split()]
            obj_level = floor(log2(people)) + 1
            stalls_count = defaultdict(int)
            stalls_count[stalls] = 1
            tuples_count = defaultdict(int)
            for j in range(obj_level):
                stalls_count_bis = defaultdict(int)
                for stalls, count in stalls_count.items():
                    if stalls % 2 == 0:
                        stalls_count_bis[stalls/2] += count
                        stalls_count_bis[stalls/2 - 1] += count
                        if j == obj_level-1:
                            tuples_count[(stalls/2, stalls/2 - 1)] += count
                    else:
                        k = floor(stalls/2)
                        stalls_count_bis[k] += 2*count
                        if j == obj_level-1:
                            tuples_count[(k, k)] += count
                stalls_count = stalls_count_bis
            order = people - 2**(obj_level-1) + 1
            tup_c_list = list(tuples_count.items())
            tup_c_list = sorted(tup_c_list, key=lambda x: x[0][0]+x[0][1],
                                reverse=True)
            if order <= tup_c_list[0][1]:
                outp.write("Case #" + str(i+1) + ": " +
                           str(int(tup_c_list[0][0][0])) + " " +
                           str(int(tup_c_list[0][0][1])) + "\n")
            elif order <= tup_c_list[0][1] + tup_c_list[1][1]:
                outp.write("Case #" + str(i+1) + ": " +
                           str(int(tup_c_list[1][0][0])) + " " +
                           str(int(tup_c_list[1][0][1])) + "\n")
            else:
                outp.write("Case #" + str(i+1) + ": " +
                           str(int(tup_c_list[2][0][0])) + " " +
                           str(int(tup_c_list[2][0][1])) + "\n")
