#! /usr/bin/env python

FILE_NAME = 'D-large'

def run_once(in_file):
    num = int(in_file.readline())
    N = map(float, in_file.readline().rstrip().split(' '))
    K = map(float, in_file.readline().rstrip().split(' '))
    N.sort()
    K.sort()

    NN = list(N)
    KK = list(K)
    DW = 0
    while len(NN) > 0:
        Nmx = max(NN)
        Kmx = max(KK)
        if Nmx > Kmx:
            Kmn = min(KK)
            DW += 1
            for n in NN:
                if n < Nmx and n > Kmn:
                    Nmx = n
            NN.remove(Nmx)
            KK.remove(Kmn)
        else:
            NN.remove(min(NN))
            KK.remove(Kmx)
    
    NN = list(N)
    KK = list(K)
    W = 0
    while len(NN) > 0:
        Nmx = max(NN)
        Kmx = max(KK)
        if Nmx > Kmx:
            W += 1
            NN.remove(Nmx)
            KK.remove(min(KK))
        else:
            NN.remove(Nmx)
            KK.remove(Kmx)

    return str(DW) + ' ' + str(W)

    
in_file = open(FILE_NAME + '.in', 'r')
out_file = open(FILE_NAME + '.out', 'w')

num = int(in_file.readline())
for i in range(num):
    out_file.write('Case #' + str(i + 1) + ': ' + run_once(in_file) + '\n')
