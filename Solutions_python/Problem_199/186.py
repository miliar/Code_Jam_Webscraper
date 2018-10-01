#! /usr/bin/python

import sys

def read_case(f):
    line = read_line(f, str)
    pancakes = line.split(' ')[0]
    size_flipper = int(line.split(' ')[1])
    return pancakes, size_flipper

def solve(case):
    pancakes, size_flipper = case
    num_flips = 0
    pancakes = list(pancakes)
    for idx in range(len(pancakes)-size_flipper+1):
        if pancakes[idx] == '-':
            # flipperoo
            for i in range(size_flipper):
                if pancakes[idx+i] == '-':
                    pancakes[idx+i] = '+'
                else:
                    pancakes[idx+i] = '-'
            num_flips += 1
    if all(c == '+' for c in pancakes):
        return num_flips
    else:
        return "IMPOSSIBLE"

# Edit over here --------

def read_space_line(f, constr):
    # Reads a space-delimited line with constructor.
    line = f.readline().strip().split(' ')
    return tuple(int(x) for x in line)

def read_line(f, constr):
    return constr(f.readline().strip())

def input_iterator(in_fn):
    with open(in_fn) as f:
        num_cases = read_line(f, int)
        for i in range(num_cases):
            yield read_case(f)

def write_output(f, case_n, sol_str):
    f.write("Case #%d: %s\n" % (case_n, sol_str))

def main():
    in_fn = sys.argv[1] 
    out_fn = sys.argv[2]
    
    with open(out_fn, 'w') as out_f:
        for i, case in enumerate(input_iterator(in_fn)):
            sol_str = solve(case)
            write_output(out_f, i+1, sol_str)

if __name__ == "__main__":
    main()


