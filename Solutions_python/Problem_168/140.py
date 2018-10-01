# Eric Lee < e@ericdlee.com >
# Google Code Jam 2015
# 
# Usage: python A.py small
# list(next()) # List of chars
# [int(n) for n in next().split()] # List of ints
# If multiline, return a list of strings. Else, return a string.

import os, sys, math, fractions

def solve_case(next):
    
    R, C = [int(n) for n in next().split()]
    grid = [list(next()) for r in range(R)]
    change = 0
    def all_directions(x, y):
        ret = []
        for d in [(1,0),(0,1),(-1,0),(0,-1)]:
            i, j = x, y
            while True:
                i += d[0]
                j += d[1]
                if not (i >= 0 and j >= 0 and i < R and j < C):
                    ret.append(False)
                    break
                elif grid[i][j] != '.':
                    ret.append((i,j))
                    break
        return ret

    for i in range(R):
        for j in range(C):
            x = grid[i][j]
            if x != '.':
                all_d = all_directions(i, j)
                print all_d
                if (x == 'v' and all_d[0]) or (x == '>' and all_d[1]) or (x == '^' and all_d[2]) or (x == '<' and all_d[3]):
                    print "Found one!"
                    continue
                elif any(all_d):
                    print "New direction"
                    change += 1
                else:
                    return "IMPOSSIBLE"
    return change
    






# ---------------------------------------------------------------------------- #

def solve(next, emit):
    cases = int(next())
    for case in xrange(1, cases + 1):
        sol = solve_case(next)
        if isinstance(sol, list):
            emit("Case #{0}:".format(case))
            for line in sol:
                emit(str(line))
        else:
            emit("Case #{0}: {1}".format(case, str(sol)))
        print "{0} / {1}".format(case, cases)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python {0} small".format(sys.argv[0]))
        exit()
    prefix = sys.argv[0][:-3] + "-" + sys.argv[1]
    suffix = ".in"
    for file in os.listdir(os.path.dirname(os.path.realpath(__file__))):
        if file.startswith(prefix) and file.endswith(suffix):
            print "Loading " + file
            file_in = open(file, "r")
            file_out = open(file[:-3] + ".out", "w")
            solve(lambda: file_in.readline().strip(), lambda x: file_out.write(str(x) + "\n"))
            file_in.close()
            file_out.close()
            print "Complete."
