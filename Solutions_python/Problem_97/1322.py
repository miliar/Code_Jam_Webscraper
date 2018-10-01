#!/usr/bin/python2.7


from sys import argv, stdin, stdout
#from math import log10, pow 

inf, ouf = stdin, stdout
cache = {}

def recycledNumbers(n, A, B):

    c = 0
    s = n
    ns = []

    ndigits = len(str(n))-1
    m = int(10.0 ** ndigits)

    while True:
        r = s % 10
        s = s / 10
        s = s + m * r

        if s == n:
            break

        if len(str(s))-1 == ndigits:
            ns.append(s)

    return ns


def logger(case, output):
    ouf.write("Case #%d: %s\n" %(case, output))
    ouf.flush()


def main():
    T = int(inf.readline())
    for x, line in enumerate(inf.readlines(), 1):
        A, B = [int(i) for i in line.split()]

        y = len(filter(lambda x: A<= x <= B, cache.get(x, [])))
        if y == 0:
            y = 0
            for i in xrange(A, B+1):
                y += len(filter(lambda x: A<=x<= B, recycledNumbers(i, A, B)))

        logger(x, y/2)
    

if __name__ == '__main__':
    main()

