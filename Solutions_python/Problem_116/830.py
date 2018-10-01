from __future__ import print_function, division

from bisect import bisect_left

import sys

infile = open(sys.argv[1])
outfiles = (sys.stdout, open(sys.argv[2], 'w'))

def read_in(infile):
    data = infile.readlines()
    amount = int(data[0])
    content = [s.strip() for s in data[1:] if s != '\n']
    content = [content[i*4:i*4+4] for i in range(0,amount)]
    assert amount == len(content)
    return content

def do_output(number, output, outfiles):
    for f in outfiles:
        print('Case #%d: ' % number, output, file=f)

def main():
    for i, content in enumerate(read_in(infile)):
        do_output(i+1, do_task(content), outfiles)



def do_task(content):
    full = True
    pOd1 = pOd2 = pXd1 = pXd2 = True
    for i in range(0,4):
        if(content[i][i] != 'O' and content[i][i] != 'T'):
            pOd1 = False
        if(content[i][i] != 'X' and content[i][i] != 'T'):
            pXd1 = False
        if(content[3-i][i] != 'O' and content[3-i][i] != 'T'):
            pOd2 = False
        if(content[3-i][i] != 'X' and content[3-i][i] != 'T'):
            pXd2 = False
        pOr = pOc = pXr = pXc = True
        for j in range(0,4):
            if(content[i][j] == '.'):
                full = False
            if(content[i][j] != 'O' and content[i][j] != 'T'):
                pOr = False
            if(content[i][j] != 'X' and content[i][j] != 'T'):
                pXr = False
            if(content[j][i] != 'O' and content[j][i] != 'T'):
                pOc = False
            if(content[j][i] != 'X' and content[j][i] != 'T'):
                pXc = False
        if(pOr or pOc):
            return 'O won'
        if(pXr or pXc):
            return 'X won'
    if(pOd1 or pOd2):
        return 'O won'
    if(pXd1 or pXd2):
        return 'X won'
    if(full):
        return 'Draw'
    else:
        return 'Game has not completed'

if __name__=='__main__':
    main()
    #read_in(infile)
