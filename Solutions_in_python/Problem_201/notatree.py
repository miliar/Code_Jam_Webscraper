import numpy as np
import pandas as pd

lines = []
df = pd.read_csv('C-small-1-attempt0.in',header=None,index_col=None)
S = int(df.values[0][0])


###
print df
for i in xrange(1,S+1):
	s = df.values[i][0]
	n, k = s.split()
	N = int(n)
	K = int(k)

	stack = [N]
	x = -1
	y = -1

	for l in xrange(K):
		m = stack.pop()
		if l!=K-1:
			if m == 1:
				stack.append(0)
				stack.append(0)
			elif m % 2 == 0:
				mm = m/2
				stack.append(mm-1)
				stack.append(mm)
			else:
				mm = (m-1)/2
				stack.append(mm)
				stack.append(mm)
			stack = sorted(stack)
		else:
			if m == 1:
				x = 0
				y = 0
			elif m % 2 == 0:
				x = m/2
				y = x-1
			else:
				x = (m-1)/2
				y = x
			
	lines.append(r'Case #' + str(i) + ': ' + str(x) + ' ' + str(y))

print lines
###


with open("mout.txt", "w") as text_file:
	for line in lines:
			text_file.write(line + "\n")
