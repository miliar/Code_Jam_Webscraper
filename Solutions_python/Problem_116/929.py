#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools, collections
import sys
import math
import fractions
import string

def input_read(filename):
    data = None
    with open(filename) as f:
        for x in f:
            yield x.strip()

def output_file(filename, ans):
    with open(filename, 'w') as f:
        for n, a in enumerate(ans,1):
            f.write('Case #%d: ' % n)
            if a == 'X':
                f.write('X won\n')
            elif a == 'O':
                f.write('O won\n')
            elif a == 'D':
                f.write('Draw\n')
            else:
                f.write('Game has not completed\n')
    return

def gen_testcase(ifilename):
    itr = input_read(ifilename)
    T = next(itr)
    for x in range(int(T)):
        f = list()
        for l in range(4):
            f.append(next(itr))
        yield f
        #skip blank line
        next(itr)

def make_direction(field):
    for y in range(4):
        yield [field[y][x] for x in range(4)]
    for x in range(4):
        yield [field[y][x] for y in range(4)]
    #diagonal
    yield [field[x][x] for x in range(4)]
    yield [field[3-x][x] for x in range(4)]

def solve_one(field):
    #print(field)
    direction = make_direction(field)
    game_ended = True
    for line in direction:
        #print(line)
        result = check_four(line)
        if result == 'X' or result == 'O':
            return result
        elif result == '.':
            game_ended = False

    if game_ended:
        return 'D'
    else:
        return 'E'

def check_four(data):
    if '.' in data:
        return '.'
    elif 'X' in data and 'O' in data:
        return 'F'
    else:
        if 'X' in data:
            return 'X'
        elif 'O' in data:
            return 'O'
        assert("never happened")

def solve_all(inputfile):
    for field in gen_testcase(inputfile):
         yield solve_one(field)

def main(ifile, ofile):
    output_file(ofile, solve_all(ifile))
    return

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    #parser.add_option('-i', type='string', dest='ifile', help='input filename', default='input.txt')
    parser.add_option('-o', type='string', dest='ofile', help='output filename', default='output.txt')
    
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.print_help()
        sys.exit()

    try:
        main(args[0], options.ofile)
    except IOError as data:
        print(data)

