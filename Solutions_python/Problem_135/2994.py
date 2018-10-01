import sys
import math

def main():
    #infile = open('A-large.in')
    #infile = open('in')
    infile = open('A-small-attempt0.in')
    #infile = open('A-small-practice.in')
    #infile = open('A-large-practice.in')
    outfile = open('out', 'w')
    T = long(infile.readline())
    for i in xrange(T):
        outfile.write('Case #'+str(i+1)+': ' + solve(infile) + '\n')

def solve(f):
    r1 = int(f.readline())
    sq1 = [map(long, f.readline().split()) for i in range(4)]
    r2 = int(f.readline())
    sq2 = [map(long, f.readline().split()) for i in range(4)]
    ans = list(set(sq1[r1-1]) & set(sq2[r2-1]))
    res = ''
    if len(ans) == 0:
        res = 'Volunteer cheated!'
    elif len(ans) == 1:
        res = str(ans[0])
    else:
        res = 'Bad magician!'
    return res

if __name__=='__main__':
    main()
