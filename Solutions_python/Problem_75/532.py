#!/usr/bin/python

import sys

f = open("mag.in","rb")
t = int(f.readline())

for i in range(t):
	com = {}
	opp = {}
	def magic(f):
		n = len(f)
		if (n >= 2):
			loc = (f[n-1],f[n-2])
			if (loc in com):
				f[n-2] = com[loc]
				f.pop()
				magic(f)
			else:
				for i in range(n-1):
					if ((f[i],f[n-1]) in opp):
						del f[:]
						break
	
	s = f.readline().split()
	c = int(s.pop(0))
	for j in range(c):
		ch = s.pop(0)
		com[(ch[0],ch[1])] = ch[2]
		com[(ch[1],ch[0])] = ch[2]
	d = int(s.pop(0))
	for k in range(d):
		ch = s.pop(0)
		opp[(ch[0],ch[1])] = True
		opp[(ch[1],ch[0])] = True
	n = int(s.pop(0))
	st = s.pop(0)
	final = []
	for l in range(n):
		final.append(st[l])
		magic(final)
	sys.stdout.write("Case #"+str(i+1)+": [")
	if (len(final) > 0):
		for j in range(len(final)-1):
			sys.stdout.write(final[j]+", ")
		sys.stdout.write(final[len(final)-1])
	sys.stdout.write("]\n")
