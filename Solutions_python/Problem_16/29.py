from __future__ import with_statement
from contextlib import nested
import sys
from time import time

def permutes(st):
	if len(st) == 1:
		yield st
		return
	for i in range(len(st)):
		newst = st[:i] + st[i+1:]
		for perm in permutes(newst):
			yield (st[i],) + perm

def permute_block(perm, block):
	return ''.join(block[i] for i in perm)

def permute_text(perm, text):
	l = len(perm)
	blocks_num = len(text) // l
	return ''.join(permute_block(perm, text[i*l:(i+1)*l]) for i in xrange(blocks_num))

def calc_rle(text):
	cnt = 0
	last = None
	for c in text:
		if last != c:
			cnt += 1
			last = c
	return cnt
		

def do_case(fit):
	k = map(int, fit.next().split(' '))[0]
	text = fit.next().strip(' \n\r\t')
	return min(calc_rle(permute_text(perm, text))
			   for perm in permutes(tuple(range(k))))
	

def do_all(fin, fout):
	start = time()
	with nested(file(fin), file(fout, 'w')) as (fi, fo):
		fit = iter(fi)
		case_num = int(fit.next())
		for i in range(1, case_num+1):
			fo.write("Case #%d: %s\n" % (i, do_case(fit)))
	print "Execution time:", time() - start

use_psyco = True

if __name__ == '__main__':
	if use_psyco:
		try:
			import psyco
			psyco.full()
			print "Optimized with Psyco"
		except ImportError:
			pass
	do_all(*sys.argv[1:3])
