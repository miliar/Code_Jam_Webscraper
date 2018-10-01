#!/usr/bin/env python
# google code jam 2011
# round 1c, problem c
# Joseph Lee <GengarKhan@gmail.com>
# 5/22/11

import sys

def main(name_in, name_out):
    infile = open(name_in, 'r').read().strip().split('\n')[1:]  # input 1st arg
    if name_out != None:
        outfile = open(name_out, 'w')    # output file, 2nd cmd-line arg
    else:
        outfile=sys.stdout
    casenum=1
    while len(infile) > 0:
        N, L, H=infile.pop(0).strip().split(' ')
        N=int(N)
        L=int(L)
        H=int(H)
        temp=infile.pop(0).strip().split(' ')
        Nlist=[]
        while len(temp) > 0:
            Nlist.append(int(temp.pop(0)))
        outfile.write('Case #%d: %s\n'%(casenum, test_case(L, H, Nlist)))
        casenum=casenum+1
    if outfile != sys.stdout:
        outfile.close()
    return 0

# main test case calculation method
def test_case(L, H, Nlist):
    c=L
    while c <= H:
        count=0 # non-harmony count
        for i in Nlist:
            if i > c:
                if i % c != 0:
                    count+=1
            else:
                if c % i != 0:
                    count +=1
        if count == 0:
            return str(c)
        c+=1
    return 'NO'


# parse input from command line
def parse_input(test_in):
    return None



if __name__=='__main__':
    name_in=sys.argv[1]
    if len(sys.argv) >= 3:
        name_out=sys.argv[2]
    else:
        name_out=None
    main(name_in, name_out)

