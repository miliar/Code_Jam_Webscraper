import sys
import math

def main():
    #infile = open('in')
    infile = open('D-small-attempt2.in')
    #infile = open('D-large.in')
    #infile = open('D-small-practice.in')
    #infile = open('D-large-practice.in')
    outfile = open('out', 'w')
    T = long(infile.readline())
    for i in xrange(T):
        outfile.write('Case #'+str(i+1)+': ' + solve(infile) + '\n')

def solve(infile):
    x, r, c = map(long, infile.readline().split())
    if r > c:
        r, c = c, r
    if x == 1:
        return 'GABRIEL'
    elif x == 2:
        if c >= 2 and (c*r % 2 == 0):
            return 'GABRIEL'
        else:
            return 'RICHARD'
    elif x == 3:
        if c < 3 or r == 1:
            return 'RICHARD'
        elif (c*r % 3 == 0):
            return 'GABRIEL'
        else:
            return 'RICHARD'
    elif x == 4:
        if c == 4 and r >= 3:
            return 'GABRIEL'
        else:
            return 'RICHARD'
    elif x > r and x > c:
        return 'RICHARD'
    elif x >= 7:
        return 'RICHARD'
    elif x > 2*r:
        return 'RICHARD'
    else:
        
        n = r*c - x
        if n % x == 0:
            return 'GABRIEL'
        else:
            return 'RICHARD'
    return 'GABRIEL'
    #return '{:0.7f}'.format(res)

if __name__=='__main__':
    main()
