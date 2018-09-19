#!/usr/bin/env python

dd = {}
ds = 'ay,bh,ce,ds,eo,fc,gv,hx,id,ju,ki,lg,ml,nb,ok,pr,qz,rt,sn,tw,uj,vp,wf,xm,ya,zq'
for d in ds.split(','):
	pair = tuple(d)
	dd[pair[0]] = pair[1]

def main():
	import sys

	sys.stdin.readline()
	casenum = 1
	while True:
		line = sys.stdin.readline().strip()
		if line=='': break
		print 'Case #%s:' % casenum, unsub(line)
		casenum += 1


def unsub(s):
	ns = ''
	for char in s:
		try: ns += dd[char]
		except KeyError: ns += char
	return ns

if __name__ == '__main__': main()
