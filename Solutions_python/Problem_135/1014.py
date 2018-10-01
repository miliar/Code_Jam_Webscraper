#!/usr/bin/env python
import sys
if __name__ == "__main__":
    input = open(sys.argv[1])
    T = int(input.readline())
    for ncase in xrange(1, T + 1):
        row1 = int(input.readline())
        matrix1 = [set(map(int,input.readline().split())) for i in xrange(4)] 
        row2 = int(input.readline())
        matrix2 = [set(map(int,input.readline().split())) for i in xrange(4)] 
        guess = matrix1[row1 - 1] & matrix2[row2 - 1]
        print "Case #%d:"%ncase,
        if len(guess) == 1:
            print guess.pop()
        elif len(guess) == 0:
            print "Volunteer cheated!"
        else:
            print "Bad magician!"
