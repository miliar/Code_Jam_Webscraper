#!/usr/env/bin/python
from sys import argv
import re

if len(argv) < 2:
    print("Insufficient arguments. Usage: python script.py <input file> [<output file>]")
    exit()

input_file = open(argv[1])

output_file = None
if len(argv) >= 3:
    output_file = open(argv[2], 'w')

n = int(input_file.readline())

i = 1
while i <= n:
    (N, M) = map(int, input_file.readline()[:-1].split(" "))
    
    tree = dict()
    while N > 0:
        chunks = input_file.readline()[:-1].split('/')[1:]
        node = tree
        while len(chunks) != 0:
            chunk = chunks.pop(0)
            if not chunk in node:
                node[chunk] = dict()
            node = node[chunk]
        N -= 1
    
    res = 0
    while M > 0:
        chunks = input_file.readline()[:-1].split('/')[1:]
        node = tree
        while len(chunks) != 0:
            chunk = chunks.pop(0)
            if not chunk in node:
                node[chunk] = dict()
                res += 1
            node = node[chunk]
        M -= 1
    
    res = 'Case #' + str(i) + ': ' + str(res)
    print(res)
    if output_file is not None:
        output_file.write(res + '\n')
    i += 1

input_file.close()
if output_file is not None:
    output_file.close()
