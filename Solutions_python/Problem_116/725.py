#!/usr/bin/env python

def main():
    lines = [list(read())[:-1] for i in range(4)]
    cols = [[lines[i][j] for i in range(4)] for j in range(4)]
    diags = [[lines[i][i] for i in range(4)], [lines[i][3-i] for i in range(4)]]
    for l in lines + cols + diags:
        for c in ['O', 'X']:
            if all(i == c or i == 'T' for i in l):
                return c + ' won'
    for l in lines:
        for c in l:
            if c == '.':
                return 'Game has not completed'
    return 'Draw'


# Parameters:
PROBLEM = 'A'
INPUT_SIZE = 'large' # None to read from command line
INPUT_ID = '' # None to read from command line
INPUT_FILE = '{problem}-{input_size}{input_id}.in' # None for stdin
OUTPUT_FILE = '{problem}-{input_size}{input_id}.out' # None for stdout

# Bootstrap:


import os
import sys

in_stream = sys.stdin
out_stream = sys.stdout
download_dir = os.path.expanduser('~/Downloads')

def read(f=None):
    return f(in_stream.readline()) if f is not None else in_stream.readline()

def read_array(f=str, split=None):
    return map(f, read(f).split(split))

def write(s):
    out_stream.write(s)

def init(problem, input_size, input_id, in_file, out_file):
    global in_stream
    global out_stream
    if in_file is not None or out_file is not None:
        if len(sys.argv) == 3:
            input_size = sys.argv[1]
            input_id = sys.argv[2]
        elif len(sys.argv) == 1 and (input_size is None or input_id is None):
            sys.stderr.write('Usage: main.py [[input_size] input_id]\n')
            sys.stderr.write('Error: input_size and input_id must be provided in main.py or on the command line\n')
            sys.exit(1)
        elif len(sys.argv) == 2:
            if input_size is None:
                input_size = sys.argv[1]
            else:
                input_id = sys.argv[1]
    if in_file is not None:
        in_file = in_file.format(problem=problem, input_size=input_size, input_id=input_id)
        down_path = os.path.join(download_dir, in_file)
        if not os.path.exists(in_file) and os.path.exists(down_path):
            os.system('mv "{}" "{}"'.format(down_path, in_file))
        in_stream = open(in_file, 'r')
    if out_file is not None:
        out_file = out_file.format(problem=problem, input_size=input_size, input_id=input_id)
        out_stream = open(out_file, 'w')

if __name__ == '__main__':
    init(PROBLEM, INPUT_SIZE, INPUT_ID, INPUT_FILE, OUTPUT_FILE)
    T = read(int)
    for t in range(1,T+1):
        write('Case #{0}: {1}\n'.format(t, main()))
        read()
