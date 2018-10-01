#!/usr/bin/env python

import sys

def attempt(moz):
    
    for y in range(len(moz)):
        for x in range(len(moz[0])):
            if moz[y][x] == '#':
                result = place_red(x, y, moz)
                if result is False:
                    return False
                else:
                    moz = result
    return moz

def output_result(case, result):
    print "Case #%s:" % (case+1,)
    if not result:
        print "Impossible"
    else:
        for line in result:
            print ''.join(line)

def place_red(x, y, moz):
    if moz[y][x] != '#':
        return moz
    try:
        if moz[y][x] == moz[y+1][x] == moz[y][x+1] == moz[y+1][x+1] == '#':
            moz[y][x] = '/'
            moz[y+1][x] = '\\'
            moz[y][x+1] = '\\'
            moz[y+1][x+1] = '/'
            return moz
        else:
            return False
    except IndexError:
        return False

if __name__ == '__main__':
    in_path = sys.argv[1]
    with open(in_path, 'r') as in_file:
        cases = int(in_file.readline())

        for case in range(cases):
            height = int(in_file.readline().split()[0])
            moz = []
            for line in range(height):
                moz.append(list(in_file.readline().strip()))
            result = attempt(moz)
            output_result(case, result)