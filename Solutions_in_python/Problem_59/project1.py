#!/usr/bin/python2.6

import os, sys, math

file = open(sys.argv[1] , 'r')
nbr_testcases = int(file.readline())

for test in range(nbr_testcases):
    N, M = tuple([int(k) for k in file.readline().split()])
    dirs = set()
    news = set()
    for i in range(N):
        existdir = file.readline().strip()
        dirs.add(existdir)
    for i in range(M):
        newdir = file.readline().strip()
        parts = newdir[1:].split('/')
        tmpdir = '/'
        for part in parts:
            tmpdir += part
            if tmpdir not in dirs:
                news.add(tmpdir)
            tmpdir += '/'
    print "Case #"+str(test+1)+": "+str(len(news))

file.close()
