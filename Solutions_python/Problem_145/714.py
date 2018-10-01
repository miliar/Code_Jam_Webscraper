import sys
from fractions import gcd
from math import log
from math import ceil

in_file = open(sys.argv[1], 'r')
out_file = open(sys.argv[2], 'w')

T = int(in_file.readline())

imp = "impossible"

for t in range(T):
	line = in_file.readline().split('/')
	nom, den = int(line[0]), int(line[1])
	comm = gcd(nom, den)
	nom = nom / comm
	den = den / comm
	
	lg = log(den, 2)
	#n = int(round(lg / nom))
	n = 1
	f = (float(nom) / den) * 2
	while n <= 40 and f < 1:
		f *= 2
		n += 1
		
	
	if lg == int(lg) and lg <= 40:
		out_file.write('Case #{0}: {1}\n'.format(t+1, n))
	else:
		out_file.write('Case #{0}: {1}\n'.format(t+1, imp))

in_file.close()
out_file.close()
