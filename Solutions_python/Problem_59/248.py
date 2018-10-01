#!/usr/bin/env python

# Google code jam 2010 : unix

import sys

def cutter(direct):
    for i in reversed(range(len(direct))):
	if direct[i] == "/":
	    return direct[:i]
    return direct

def result(news,current):
    count = 0
    for direct in reversed(sorted(news)):
	if current.count(direct) != 0:
	    continue
	else:
	    pnew = []
	    dd = direct
	    while(dd != "" and current.count(dd) == 0):
		dd = cutter(dd)
		pnew.append(dd)
		count = count + 1
	    current = current + pnew

    return count

p = int(sys.stdin.readline())
cases = []
for s in range(1,p+1):
    line = sys.stdin.readline()
    N,_,M = line.partition(' ')
    N = int(N)
    M = int(M)

    current = [[] for i in range(N)]
    for j in range(N):
	line = sys.stdin.readline()
	line,_,_ = line.partition('\n')
	current[j] = line

    news = [[] for i in range(M)]
    for j in range(M):
	line = sys.stdin.readline()
	line,_,_ = line.partition('\n')
	news[j] = line

    print "Case #" + str(s) + ": " +  str(result(news,current))

