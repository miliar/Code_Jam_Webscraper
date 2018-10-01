import numpy as np
import os
import re

def solve(amote, motes):
    if len(motes) == 0:
        return 0
    i = 0
    while (i < len(motes) and amote > motes[i]):
        amote += motes[i]
        i += 1
    if (i == len(motes)):
        return 0
    else:
        motes = motes[i:]
        delnext = 1 + solve(amote, motes[1:])
        addtoa = -1
        if (amote != 1):
            addtoa = 1 + solve(2*amote-1, motes)
        else :
            return delnext
        if (delnext > addtoa or addtoa == -1):
            return addtoa
        else :
            return delnext
    return 'ERROR!'
    

def main():
    infile = "Asmall.in"
    inf = open(infile, 'r')

    outfile = "Asmall.out"
    outf = open(outfile, 'w')

    lnum = 1
    case = 0
    totcase = 0
    amote = 0
    for line in inf:
        if (lnum == 1):
            totcase = int(line.split()[0])
        elif (lnum % 2 == 0) :
            lstring = line.split()
            amote = int(lstring[0])
            nmote = int(lstring[1])
            motes = np.zeros(nmote)
        else:
            case += 1
            lstring = line.split()
            for i in range(len(lstring)):
                motes[i] = int(lstring[i])
            motes.sort()
            min_op = solve(amote,motes)
            outf.write("Case #" + str(case) + ": " + str(min_op) + "\n")
        lnum += 1
            


if __name__ == '__main__':
     main()
