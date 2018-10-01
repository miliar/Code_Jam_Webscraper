import os
import sys

problem = sys.argv[1]
path = os.path.expanduser('~/Downloads/')
file_in = path + problem + '.in'
file_out = path + problem + '.out'

with open(file_in, 'rb') as fin, open(file_out, 'w') as fout:
    lines = fin.read().splitlines()
    case = 1
    for l in lines[1:]:
        S, K = l.split()
        row = [c == '+' for c in S]
        attempts = 0
        p1 = 0
        while True:
            try:
                p1 = row.index(False, p1)
            except ValueError:
                break
            try:
                for i in range(int(K)):
                    row[p1 + i] = not row[p1 + i]
            except IndexError:
                attempts = "IMPOSSIBLE"
                break
            attempts += 1
        fout.write("Case #%d: %s\n" % (case, attempts))
        case += 1
