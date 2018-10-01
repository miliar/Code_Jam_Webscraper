#!/usr/bin/env python
dataset = open('A-large.in', 'r').read().splitlines()
cases = dataset[0]
del(dataset[0])
xwins = open('xwins', 'r').read().splitlines()
owins = open('owins', 'r').read().splitlines()
result = ''

structure = [i.split(' ') for i in ' '.join(dataset).split('  ')]


def get_vertical(dataset):
    row1 = ''
    row2 = ''
    row3 = ''
    row4 = ''
    for a, b, c, d in dataset:
        row1 += a
        row2 += b
        row3 += c
        row4 += d
    return [row1, row2, row3, row4]


def get_diagonal(dataset):
    return [dataset[0][0]+dataset[1][1]+dataset[2][2]+dataset[3][3],
            dataset[0][3]+dataset[1][2]+dataset[2][1]+dataset[3][0]]


vertical = [get_vertical(i) for i in structure]
diagonal = [get_diagonal(i) for i in structure]
tictacstruct = [[structure[i], vertical[i], diagonal[i]]
                for i in range(len(structure))]


def checkX(case):
    for i in case:
        for j in i:
            if j in xwins:
                return 'X won'
    return None


def checkO(case):
    for i in case:
        for j in i:
            if j in owins:
                return 'O won'
    return None

resultoutput = open('result.out', 'w')

for case in range(len(tictacstruct)):
    X = checkX(tictacstruct[case])
    O = checkO(tictacstruct[case])
    if X == 'X won' and O == None:
        result = X
    elif X == None and O == 'O won':
        result = O
    elif X == None and O == None:
        result = 'Draw'
        for i in tictacstruct[case]:
            for j in i:
                if '.' in j:
                    result = 'Game has not completed'
    print 'Case #'+str(case+1)+': '+result
    resultoutput.write('Case #'+str(case+1)+': '+result+'\n')

resultoutput.close()