import sys
import math

def main():
    #infile = open('in')
    infile = open('B-small-attempt0.in')
    #infile = open('B-large.in')
    #infile = open('B-small-practice.in')
    #infile = open('B-large-practice.in')
    outfile = open('out', 'w')
    T = long(infile.readline())
    for i in xrange(T):
        outfile.write('Case #'+str(i+1)+': ' + solve(infile) + '\n')

def solve(infile):
    n = long(infile.readline())
    p = sorted(map(long, infile.readline().split()), reverse=True)
    r = p[0]
    res = p[0]

    for xi in range(p[0], 0, -1):
        for ci in range(0, res - xi + 1):
            cnt = 0
            for pi in p:
                if pi > xi:
                    cnt += pi / xi - (1 if pi % xi == 0 else 0)
                if cnt > ci:
                    break
            if cnt <= ci and (ci + xi) < res:
                res = ci + xi
    return str(res)
    #return '{:0.7f}'.format(res)

if __name__=='__main__':
    main()
