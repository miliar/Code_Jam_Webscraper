import string
import itertools
import sys

def process_case(old_dirs, new_dirs):
    dirs = set(old_dirs)
    result = 0
    for d in new_dirs:
        if (d not in dirs):
            segments = d.split('/')
            for i in range(2,len(segments)+1):
                partial = '/'.join(segments[:i])
                if (partial not in dirs):
                    dirs.add(partial)
                    result += 1
    return result

def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        old_num, new_num = line_of_numbers(next(lines))[:2]
        old_dirs = [next(lines) for i in range(old_num)]
        new_dirs = [next(lines) for i in range(new_num)]
        result = process_case(old_dirs, new_dirs)
        yield 'Case #{0}: {1}\n'.format(ci, result)
    
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

start('A-test')
