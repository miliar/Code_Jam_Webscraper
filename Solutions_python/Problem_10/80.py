from __future__ import with_statement
from contextlib import nested
import sys

def do_case(fit):
	P, K, L = map(int, fit.next().split(' '))
	freqs = sorted(map(int, fit.next().split(' ')), reverse = True)
	freqs = [freqs[i*K:(i+1)*K] for i in range(L//K + 1)]
	freqs = [sum(f) for f in freqs]
	return sum(f*(i+1) for (i,f) in enumerate(freqs))
	

def do_all(fin, fout):
	with nested(file(fin), file(fout, 'w')) as (fi, fo):
		fit = iter(fi)
		case_num = int(fit.next())
		for i in range(1, case_num+1):
			fo.write("Case #%d: %d\n" % (i, do_case(fit)))

if __name__ == '__main__':
	do_all(*sys.argv[1:3])
