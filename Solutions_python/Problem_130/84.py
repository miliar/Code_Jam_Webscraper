import sys
import math


def main():
    infile = open(sys.argv[1])
    outfile = open(sys.argv[1][:-2] + 'out', 'w')
    numcases = int(infile.readline())

    for case in range(numcases):
        N,P = (int(k) for k in infile.readline().split())
        k = 1
        maxi = 0
        while (2**N - 2**(N-k)) < P:
            k+=1

        maxi = 2**k - 2

        newP = 2**N - P

        maxj = 0
        l = 1
        while (2**N - 2**(N-l))<newP:
            l+=1
        maxj = 2**l - 2

        mini = 2**N - 2 - maxj
        if P == 2**N:
            mini = 2**N - 1
            maxi = 2**N - 1
        out = '%d %d' % (maxi, mini)
        print(out)
        print('Case #%d:' % (case + 1), out, file=outfile)



if __name__ == '__main__':
    main()
