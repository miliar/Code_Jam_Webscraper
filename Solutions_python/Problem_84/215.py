#! /usr/bin/env python
# vim: set et ts=4 sw=4 ci cino=(0:
import sys
import os
import math
import binascii
                            
def main():
    f = open(sys.argv[1])
    ntest = int(f.readline().strip())

    for nt in xrange(ntest):
        l = f.readline().strip().split()  
        if len(l) !=  2:
            print "Error got ", l
            sys.exit(1)

        r = int(l[0])
        c = int(l[1])
        pic = []
        for i in xrange(r):
            l = f.readline().strip().split()  
            if len(l) !=  1 and len(l[0]) != c:
                print "Error got team", l
                sys.exit(1)
            pic.append(list(l[0]))

        res = True
        for i in xrange(r):
            for j in xrange(c):
                if ( pic[i][j] == "#" ):
                    pic[i][j] = "/"
                    if ( j == c - 1 or pic[i][j+1] != "#" ):
                        res = False
                        break
                    else:
                         pic[i][j+1] = "\\"

                    if ( i == r - 1 or pic[i + 1][j] != "#" ):
                        res = False
                        break
                    else:
                         pic[i+1][j] = "\\"

                    if ( pic[i+1][j+1] != "#" ):
                        res = False
                        break
                    else:
                         pic[i+1][j+1] = "/"

            if res == False:
                break

        print "Case #%d:" % (nt + 1)
        if ( res ):
            for i in xrange(r):
                print "".join(pic[i])
        else:
            print "Impossible"

if __name__ == "__main__":
    main()

