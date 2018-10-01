# -*- coding: utf-8 -*-
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
from math import floor

def load_file(filename):
    in_file = open(filename, encoding='utf-8')
    content = in_file.readlines()
    return content

def writeStringToFile(output, filename):
    out_file = open(filename + '.out', 'w')
    for i in output:
        out_file.write(i + '\n')
    out_file.close()

OCCUPIED = 'O'
EMPTY = '.'

def init(N):
    status = OCCUPIED
    for i in range(N):
        status += EMPTY
    status += OCCUPIED
    return status  

def choose(status):
    splits = status.split(OCCUPIED)
    maxlen = 0
    maxidx = -1
    for i in range(len(splits)):
        if len(splits[i]) > maxlen:
            maxlen = len(splits[i])
            maxidx = i
    if maxlen % 2 == 0:
        splits[maxidx] = int(maxlen/2 - 1) * EMPTY + OCCUPIED +  int(maxlen/2) * EMPTY
        l = int(maxlen/2 - 1)
    else:
        splits[maxidx] = int(maxlen/2) * EMPTY + OCCUPIED +  int(maxlen/2) * EMPTY
        l = int(maxlen/2)
    r = int(maxlen/2)
    status = OCCUPIED.join(splits)
    return status, l, r

def solve(line):
    N, K = int(line.split()[0]), int(line.split()[1])
    status = init(N)
    for i in range(K):
        status, l, r = choose(status)
    return str(max(l, r)) + ' ' + str(min(l, r))

if __name__ == "__main__":
    filename = "C-small-1-attempt0.in"
    file = load_file(filename)
    n = int(file[0])
    out = []
    for i in range(1, n+1):
        line = file[i]
        out.append("Case #{0}: {1}".format(i, solve(line)))
#print(out)
writeStringToFile(out, filename)
