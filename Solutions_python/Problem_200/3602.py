#!/usr/bin/python3

import sys
infile = sys.argv[1]
try:
    outfile = sys.argv[2]
except IndexError:
    outfile = sys.stdout

def read_int(f):
    return int(f.readline())

def read_ints(f, sep=" "):
    return map(int, f.readline().rstrip().split(sep))

def read_lines(f, no_lines):
    retval = []
    for i in range(no_lines):
        retval.append(f.readline().rstrip())
    return retval



def get_break(n):
    if n<10:
        return -1
        
    n_s = str(n)
    old_digit = n_s[0]
    retval_s = n_s[0]
    
    for idx, digit in enumerate(n_s[1:]):
        if digit < old_digit:
            retval_s += "0"*(len(n_s)-1-idx)
            return int(retval_s)
        else:
            old_digit = digit
            retval_s += digit
            
    return -1
    

def solve(n):
    cnt = 0
    while True:
        cnt += 1
#        print(n)
        new = get_break(n)
        if new == -1:
            return (n, cnt)
        else:
            n = new -1 


def main():
    f = open(infile, "r")
    no_cases = read_int(f)

    out = open(outfile, "w")
    
    for case_idx in range(no_cases):
        n = read_int(f)
        sol, cnt = solve(n)
        out.write("Case #%d: %s\n" % (case_idx+1, sol))
    
    f.close()
    out.close()
            

if __name__ == "__main__":
    main()
    

