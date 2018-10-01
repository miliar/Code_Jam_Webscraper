import numpy as np

inname = "input.txt"
outname = "output.txt"

with open(inname, 'r') as f:
	cases = int(f.readline())
	for tc in range(1,cases+1):
		line = f.readline().strip().split(' ')
		D = int(line[0])
		N = int(line[1])
		maxtime = 0
		for i in range(N):
			line = f.readline().strip().split(' ')
			Ki = int(line[0])
			Si = int(line[1])
			t = (D - Ki) / Si
			if t > maxtime:
				maxtime = t

		print("Case #%d: %.6f" % (tc, D/maxtime))
