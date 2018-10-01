#!/usr/bin/env python

import sys

lines = open(sys.argv[1], 'r').readlines()

T = int(lines[0])

def parse_test(test):
	bits = test.split(' ')

	i = 0
	C = int(bits[i])
	
	i += 1
	bases = []
	for j in xrange(C):
		bases.append(bits[i+j])
	i += C
	D = int(bits[i])
	i += 1
	opps = []
	for j in xrange(D):
		opps.append(bits[i+j])
	i += D
	N = int(bits[i])
	i += 1
	
	return bases, opps, bits[i]

def build_bmap(bases):
	bmap = {}
	for base in bases:
		b1 = base[0]
		b2 = base[1]
		r = base[2]
		if not b1 in bmap:
			bmap[b1] = {}
		if not b2 in bmap:
			bmap[b2] = {}
		bmap[b1][b2] = r
		bmap[b2][b1] = r
	return bmap

def build_omap(opps):
	omap = {}
	for opp in opps:
		if not opp[0] in omap:
			omap[opp[0]] = []
		if not opp[1] in omap:
			omap[opp[1]] = []
		omap[opp[0]].append(opp[1])
		omap[opp[1]].append(opp[0])
	return omap

case = 0
for test in lines[1:T+1]:
	case += 1
	bases, opps, elems = parse_test(test.rstrip())

	bmap = build_bmap(bases)
	omap = build_omap(opps)

	l = []
	for e in elems:
		if len(l) == 0:
			l.append(e)
			continue
		if e in bmap and l[-1] in bmap[e]:
			l.append(bmap[e][l.pop()])
		elif e in omap:
			for o in omap[e]:
				if o in l:
					# poof!
					l = []
			if len(l) != 0:
				# no opps, just add it.
				l.append(e)
		else:
			l.append(e)
	
	outstr = ""
	for e in l:
		outstr += e + ', '
	print "Case #%d: [%s]"%(case, outstr[:-2])

