#!/usr/bin/env python
# -*- coding:utf-8 -*-

def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(N, foo):
        res = []
        for _ in xrange(N):
                res.append(foo())
        return res
def readlinearray(foo): return map(foo, raw_input().split())

mm = {}
out1='our language is impossible to understandzq'
out2='there are twenty six factorial possibilities'
out3='so it is okay if you want to just give up'
in1='ejp mysljylc kd kxveddknmc re jsicpdrysiqz'
in2='rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
in3='de kr kd eoya kw aej tysr re ujdr lkgc jv'

def fill(inn, outt):
	for i in xrange(len(inn)):
		mm[inn[i]] = outt[i]

fill(in1, out1)
fill(in2, out2)
fill(in3, out3)

def map_line(line):
	new_line = ''
	for l in line:
		new_line += mm.get(l, l)
	return new_line

if __name__ == '__main__':
    C = readint()
    for c in xrange(1, C+1):
		line = raw_input()
		line = map_line(line)
		print 'Case #%d: %s' % (c, line)
