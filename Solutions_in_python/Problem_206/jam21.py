from math import floor, ceil
from collections import Counter
import numpy as np

o = ""
cases = []

with open("A-large.in", "r") as input:
	T = int(input.readline())
	for t in range(T):
		
		D,N = map(int, input.readline().split()) # N ingredients and P packages
		K = []
		S = []
		tem = []
		for i in range(N):
			Ki,Si = map(int, input.readline().split())
			ti = (D-Ki)/Si
			K.append(Ki)
			S.append(Si)
			tem.append(ti)
		# print(tem)
		# print(D, N, K, S)
		temax = max(tem)
		# print(D, temax)
		s = D/temax
		print("Case #" + str(t+1) + ":", s)
		


# print(o)
	
# with open("output.txt", "w") as output:
	# output.write(o)
	