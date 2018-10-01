#!/usr/bin/python

import sys

def getl():
	return sys.stdin.readline().rstrip()

text = 'welcome to code jam'

def find_indexes(s, ch, p=-1, l=None):
	if l is None:
		l = []
	pos = s.find(ch, p+1)
	if pos == -1:
		return l
	else:
		l.append(pos)
		return find_indexes(s, ch, pos, l)

def count(text, m, p=0, n=-1):
	l = filter(lambda x: x>n, m[text[p]])
	if p == len(text)-1:
		return len(l)
	else:
		return sum(count(text, m, p+1, x) for x in l)

n = int(getl())

for i in range(n):
	line = getl()
	line = filter(lambda c: c if c in 'welcomtdja ' else '', line)
	m = {}
	for j in 'welcomtdja ':
		m[j] = find_indexes(line, j)
	#m['j'] = filter(lambda x: x>max(m[' ']), m['j'])
	#m['a'] = filter(lambda x: x>max(m['j']), m['a'])
	print('Case #{0}: {1}'.format(i+1, str(count(text,m))[-4:].zfill(4)))	
