# python 3
import string
import itertools
import sys

def avg(x):
    return sum(x) / len(x)

def process_case(n, tab):
    nlost = [tab[i].count('0') for i in range(n)]
    nwon = [tab[i].count('1') for i in range(n)]
    ngames = [nlost[i] + nwon[i] for i in range(n)]
    wp = [nwon[i] / ngames[i] for i in range(n)]
    owp = [avg([(nwon[j] - int(tab[j][i])) / (ngames[j]-1)
                   for j in range(n) if tab[i][j] != '.'])
                for i in range(n)]
    oowp = [avg([owp[j] for j in range(n) if tab[i][j] != '.'])
            for i in range(n)]
    rpi = [0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]
           for i in range(n)]
    return rpi

def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        n = int(next(lines))
        tab = [next(lines) for i in range(n)]
        result = process_case(n, tab)
        yield 'Case #{0}:\n'.format(ci)
        for x in result:
            yield '{0}\n'.format(x)
    
def line_of_numbers(s):
    return [int(sub) for sub in s.split()]

def input_gen(f_in):
    for line in f_in:
        if line.endswith('\n'):
            line = line[:-1]
        yield line

def start(basename):
    infile = basename + '.in'
    outfile = basename + '.out'
    f_in = open(infile, 'r')
    f_out = open(outfile, 'w')
    f_out.writelines(result_gen(input_gen(f_in)))
    f_in.close()
    f_out.close()

##start('A-test')
##start('A-small-attempt0')
start('A-large')
