__author__ = 'lowikchanussot'


def solve(line) :
    tok = line.split()
    #smax = int(tok[0])
    ns = [int(s) for s in tok[1]]

    n_standing = 0
    n_to_add = 0
    for i in range(len(ns)) :
        to_add = 0
        if i > n_standing :
            to_add = i - n_standing
            n_to_add += to_add
        n_standing += ns[i] + to_add
    return n_to_add


def solve_A(in_filename, out_filename):
    with open(in_filename, 'r') as file, open(out_filename, 'w') as ofile :
        lines = file.readlines()
        for case, line in enumerate(lines[1:]) :
            sol = solve(line)
            ofile.write("Case #%d: %d\n"%(case+1, sol))

if __name__ == '__main__':
    import sys
    import os
    _, input = sys.argv
    output = os.path.splitext(input)[0] + '_out.txt'
    solve_A(input, output)
