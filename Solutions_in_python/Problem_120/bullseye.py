#!/usr/bin/env python
import sys

fin = sys.stdin
fout = sys.stdout
ferr = sys.stderr

def get_io(argv):
    fin = sys.stdin
    fout = sys.stdout
    ifn = ofn = "-"
    if len(argv) == 2:
        bfn = sys.argv[1]
        ifn = bfn + '.in'
        ofn = bfn + '.out'
    if len(argv) > 2:
        ifn = argv[1]
        ofn = argv[2]
    if ifn != '-':
        fin = open(ifn, "r")
    if ofn != '-':
        fout = open(ofn, "w")
    return (fin, fout)

def get_numbers():
    line = fin.readline()
    return map(int, line.split())

def get_number():
    return get_numbers()[0]

def get_line():
    line = fin.readline()
    if len(line) > 0 and line[-1] == '\n':
        line = line[:-1]
    return line

def get_string():
    line = fin.readline()
    return line.strip()

def vlog(msg):
    sys.stderr.write("%s\n" % msg)


def bullseye_formula(r, N):
    ret = (2*r - 3)*N + 2*(N*(N+1))
    return ret

def bullseye(r, t):
    """
Divide everything by \pi.

R_n = (r+(2n-1))^2 - (r+2(n-1))^2) = 2r + 4n - 3

S_N  = \sum_{n=1}^N R_n = (2r-3)N + 4N(N+1)/2 = 2N(N+1) + (2r-3)N

Need to find max N such that S_N <= t

    2N(N+1) + (2r-3)N - t <= 0
    2N^2 + (2r-1)N - t <= 0
"""
    a = 2
    b = 2*r - 1
    c = -t
    disc = b*b - 4*a*c
    q = int(disc ** (1./2.))
    ret = (-b + q)/(2*a)
    return ret


if __name__ == "__main__":


    (fin, fout) = get_io(sys.argv)
    n_cases = get_number()
    for ci in range(n_cases):
        r = -1
        nums = get_numbers()
        result = bullseye(nums[0], nums[1])
        fout.write("Case #%d: %d\n" % (ci + 1, result))

    fin.close()
    fout.close()
    sys.exit(0)
