import heapq
import io
import sys


# from collections import *
# from itertools import *


# Scaffolding

def run(fin=sys.stdin, fout=sys.stdout):
    fin = io.StringIO(fin) if isinstance(fin, str) else fin
    N = int(fin.readline())
    for i in range(1, N + 1):
        in_line = fin.readline().rstrip('\n')
        sys.stderr.write("Case #{}: {}\n".format(i, in_line))
        t = map(int, in_line.split(' '))
        fout.write("Case #{}: {}\n".format(i, ' '.join(map(str, solve(*t)))))

def run_sample(s, n=None, fout=sys.stdout):
    s = s.strip()
    if n is not None:
        s = "1\n" + s.split('\n')[n]
    run(s, fout)

def check_sample(sample_in, expected_out):
    expected_out = expected_out.strip("\n")
    actual_out = io.StringIO()
    run_sample(sample_in, fout=actual_out)
    for line_in, line_out in zip(expected_out.split("\n"), actual_out.getvalue().strip("\n").split("\n")):
        if line_in != line_out:
            print("Expected:", line_in)
            print("Actual  :", line_out)
            break
    print("ok")

# C

def solve(N, K):
    h = []
    m = N
    for i in range(K):
        r = m // 2
        l = m - r - 1
        heapq.heappush(h, -l)
        m = -heapq.heappushpop(h, -r)
    return max(l, r), min(l, r)

# print(solve(4, 2))

run()
