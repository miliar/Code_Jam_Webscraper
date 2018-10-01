# -*- coding: UTF-8 -*-

import sys


def debug(msg):
    # return
    sys.stderr.write(msg)
    sys.stderr.flush()


def available(table, c, s_y, s_x, d_y, d_x):
    if table[d_y][d_x] != c and table[d_y][d_x] != '?':
        return False

    min_y = min(s_y, d_y)
    min_x = min(s_x, d_x)
    max_y = max(s_y, d_y)
    max_x = max(s_x, d_x)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if x == s_x and y == s_y:
                continue

            if table[y][x] != c and table[y][x] != '?':
                return False

    return True



def solve(table):
    children = []
    availables = {}
    firsts = {}
    for y in range(len(table)):
        for x in range(len(table[y])):
            c = table[y][x]
            if c != '?':
                children.append(c)
                firsts[c] = (y, x)
                availables[c] = []

    for y in range(len(table)):
        for x in range(len(table[y])):
            if table[y][x] == '?':
                for child in children:
                    c_a = firsts[child]
                    if available(table, child, c_a[0], c_a[1], y, x):
                        availables[child].append((y, x))

    #debug("availables: " + str(availables))

    for child in children:
        c_a = availables[child]
        while len(c_a) > 0:
            candidate = c_a[0]
            if not available(table, child, firsts[child][0], firsts[child][1], candidate[0], candidate[1]):
                del c_a[0]
                continue

            table[candidate[0]][candidate[1]] = child

            for i in range(len(c_a)-1, 0, -1):
                if not available(table, child, candidate[0], candidate[1], c_a[i][0], c_a[i][1]):
                    del c_a[i]

            del c_a[0]


#input_file = "A-small-attempt0.in"
#input_file = "sample.in"
input_file = "A-large.in"
f = open(input_file)
sys.stdout = open(input_file.replace(".in", ".txt"), 'w')
tc_num = int(f.readline().rstrip())

for tc in range(tc_num):
    l = f.readline().rstrip().split()
    rows = int(l[0])
    columns = int(l[1])
    table = []
    for i in range(rows):
        row = list(f.readline().rstrip())
        table.append(row)

    #debug(str(table))

    solve(table)
    #print("Case #" + str(tc + 1) + ": " + ans)
    print("Case #" + str(tc + 1) + ":")
    for row in table:
        print("".join(row))

