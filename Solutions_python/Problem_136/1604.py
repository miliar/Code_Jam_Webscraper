from __future__ import print_function, division

import sys

infile = open(sys.argv[1])
outfiles = (sys.stdout, open(sys.argv[2], 'w'))
# infile = open("b_input_large.txt")
# outfiles = (sys.stdout, open("b_out_large.txt", 'w'))


def read_in(infile):
    data = infile.readlines()
    amount = int(data[0])
    content = data[1:]
    assert amount == len(content)
    return [s.split() for s in content]


def do_output(number, output, outfiles):
    for f in outfiles:
        print('Case #%d:' % number, output, file=f)


def main():
    for i, content in enumerate(read_in(infile)):
        do_output(i+1, do_task(content), outfiles)


def do_task(content):
    n = [float(x) for x in content]
    c = n[0]      # cost of farm                         |500
    f = n[1]      # additional coin per farm             |4
    x = n[2]      # GOAL: desirable amount of coin       |2000
    s = 2.0       # initial coin production              |2
    t = {}        # dict with time needed to buy N farms
    N = 0         # number of farms

    t.setdefault(N, 0)

    while True:
        N += 1
        t.setdefault(N, c/(s + f*(N - 1)) + t[N - 1])
        current_time = t[N - 1] + x/(s + f*(N - 1))
        improved_time = t[N] + x/(s + f*N)
        if improved_time > current_time:
            return '{:0.7f}'.format(current_time)

if __name__=='__main__':
    main()
