#!/usr/bin/env python

import sys

def solve(repl, ops, invokes):
	final = []
	for i in invokes:
		final.append(i)
		if len(final) > 1:
			for r in repl:
				if (''.join(final[-2:]) == r[0:2]) or (''.join(final[-2:]) == r[0:2][::-1]):
					final.pop()
					final.pop()
					final.append(r[2])
		for o in ops:
			if (o[0] in final) and (o[1] in final):
				final = []

	return ",".join(final).replace(",", ", ")

def main(infile):
	n = int(infile.readline())
	for i in range(n):
		toks = infile.readline().split()
		c = int(toks.pop(0))
		repl = []
		for j in range(c):
			repl.append(toks.pop(0))
		d = int(toks.pop(0))
		ops = []
		for j in range(d):
			ops.append(toks.pop(0))
		m = int(toks.pop(0))
		invokes = toks.pop(0)
		print 'Case #%s: [%s]' % (i+1, solve(repl, ops, invokes))

main(sys.stdin)
