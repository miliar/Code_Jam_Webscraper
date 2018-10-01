import sys
import math

for case in range(0, int(sys.stdin.readline())):
	inputs = sys.stdin.readline()[:-1].split(" ")
	n = int(inputs[0])
	k = int(inputs[1])
	
	u = float(sys.stdin.readline()[:-1])
	
	p = sorted(list(map(float, sys.stdin.readline()[:-1].split(" "))))
	
	for i in range(0, len(p) - 1):
		if p[i] < p[i + 1]:
			if u < (p[i + 1] - p[i]) * (i + 1):
				for j in range(0, i + 1):
					p[j] += u / (i + 1)
				u = 0
				break
			else:
				u -= (p[i + 1] - p[i]) * (i + 1)
				for j in range(0, i + 1):
					p[j] = p[i + 1]
	
	chance = 1
	for i in range(0, len(p)):
		p[i] += u / len(p)
		chance *= p[i]
	
	if chance < 1e-9:
		chance = 0
	
	print("Case #" + str(case + 1) + ": " + str(chance))
