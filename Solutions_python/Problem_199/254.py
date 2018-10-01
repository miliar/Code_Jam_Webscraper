'''
Created on Apr 7, 2017

@author: fernandomendez
Oversized Pancake Flipper
'''


import argparse
import sys
import math



def get_seq(panc):
    sequence = list(panc)
    for i in range(len(sequence)):
        if sequence [i] == '+':
            sequence [i] = 0
        elif sequence [i] == '-':
            sequence [i] = 1
        else:
            sys.exit('incorrect input')
    return sequence

def solve(line):
    flips = 0
    panc, K = line.split()
    K = int(K)
    sequence = get_seq(panc)
#     print sequence
    idx =0
    while idx <= len(sequence)  - K:
#         print sequence, idx, flips
        if sequence[idx] ==1:
            for j in range(idx,idx+K):
                sequence[j] = 1-sequence[j]
            flips +=1
        idx +=1
#     print sequence
    if sum(sequence) ==0 :
        return str(flips)
    else: 
        return 'IMPOSSIBLE'


parser = argparse.ArgumentParser(description='''Template''',  epilog='')
parser.add_argument('input',  help='input file', )
parser.add_argument('output', help='output file')
args = parser.parse_args()


# mat_cases = find_all_cases(2,6)


inFile = open (args.input)
outFile = open (args.output, 'w')
line = inFile.readline()
line= line.strip()
ncases = int(line)

for case in range(1, ncases+1):
    line = inFile.readline()
    line = line.strip()

    sol = solve(line)
    outFile.write('Case #'+str(case)+": "+str(sol)+"\n")
