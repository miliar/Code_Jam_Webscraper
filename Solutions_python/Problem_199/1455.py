#!/usr/bin/python

import sys

inputFile = 'A-large.in'
f = open(inputFile, 'r')

def main(argv):
    T = int(f.readline())
    for i in range(1, T+1):
        line = f.readline()[:-1]
        S, K = line.split(' ')
        #print S, K
        tab = []
        for c in S:
            if c == '-':
                tab.append(1)
            else:
                tab.append(0)
        #print tab
        print('Case #%r: %s' % (i, countMinFlips(tab, int(K))))

def countMinFlips(tab, K):
    i, count = 0, 0

    while i <= len(tab)-K:
        if tab[i]%2 == 1:
            count = count+1
            for j in range(0, K):
                tab[i+j] += 1
        i = i+1
    for i in range(len(tab)-K+1, len(tab)):
        if tab[i] % 2 == 1:
            return 'IMPOSSIBLE'
    return str(count)

if __name__ == '__main__':
    main(sys.argv[1:])

