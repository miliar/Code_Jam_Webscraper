#!/usr/bin/env python

import sys

def main () :
    f = open(sys.argv[1])
    ncases = int(f.readline().strip())

    for icase in range(ncases) :
        n = int(f.readline())

        str = []
        for i in range(n):
            str.append(f.readline().strip())

        if n > 2 :
           print "ERROR - not implemented yet"
           continue

        chars = []
        nchar = []
        for i in range(n) :
            chars.append([])
            nchar.append([])
            last_char = ' '
            for c in str[i] :
                if not (c == last_char) :
                    last_char = c
                    chars[i].append(c)  
                    nchar[i].append(1)
                else :
                    nchar[i][-1] += 1 

#        print chars
#        print nchar

        print 'Case #%i:'%(icase+1),

        if not (''.join(chars[0]) == ''.join(chars[1])) :
            print "Fegla Won"
        else :
            solution = 0

            for i, j in zip(nchar[0], nchar[1]) :
                solution += abs(i-j)

            print solution

main()
