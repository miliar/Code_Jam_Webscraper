#!/bin/python
import sys

def get_S_p_t(line):
    items = line[:-1].split(' ')
    items = [int(i) for i in items]
    return items[1], items[2], items[3:]

def solve(S, p, t_list):
    if p <= 1:
        ast_list = [p]
    else:
        ast_list = [3 * p - 3, 3 * p - 4]

    s = 0
    for ast in ast_list:
        s += t_list.count(ast)
    s = min(s, S)
    
    for t in t_list:
        if t >= (3 * p - 2):
            s += 1
    return s

def main(file):
    outfile = file.replace('in', 'out')

    i_testcase = 0
    for line in open(file, 'r'):
        if i_testcase:
            S, p, t_list = get_S_p_t(line)
            result = solve(S, p, t_list)
            print 'Case #%d: %d\n' % (i_testcase, result)
            # SAVE
            f = open(outfile, 'a')
            f.write('Case #%d: %d\n' % (i_testcase, result))
            f.close()
        i_testcase += 1

if __name__ == '__main__':
    main(sys.argv[1])
