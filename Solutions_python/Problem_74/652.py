import sys
from collections import deque

def readline():
    return sys.stdin.readline().strip()

def solve_single(x):
    ret = deque()
    current = 1
    for i in x:
        diff = abs(i - current)
        for j in range(diff):
            ret.append('m')
        ret.append('b')
        current = i
    return ret

def move(q1, q2):
    time = 0
    while q1[0] != 'b':
        if len(q2) > 0 and q2[0] != 'b':
            q2.popleft()
        q1.popleft()
        time += 1
    q1.popleft()
    if len(q2) and q2[0] != 'b':
        q2.popleft()
    return time + 1

def solve(line):
    data = line.split()
    events = int(data[0])
    o = []
    b = []
    order = []
    for i in range(events):
        val = data[i * 2 + 1].lower()
        order.append(val)
        if val == 'o':
            o.append(int(data[i * 2 + 2]))
        else:
            b.append(int(data[i * 2 + 2]))
    os = solve_single(o)
    bs = solve_single(b)
    time = 0
    for i in order:
        if i == 'o':
            time += move(os, bs)
        else:
            time += move(bs, os)
    return time

def main():
    n_inputs = int(readline())
    for i in range(n_inputs):
        print "Case #%d: %d" % (i + 1, solve(readline()))

if __name__ == "__main__":
    main()
