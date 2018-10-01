import sys
import operator

sys.setrecursionlimit(2000)

def readn(f, n):
	return [f.readline().rstrip('\n') for i in range(n)]

fileName = "A-large"	
f = open(fileName+".in", 'r')

test = int(f.readline())

def solve(data, N, K):
	for i in range(N):
		data[i] = data[i].replace('.','')
		data[i] = "."*(N-len(data[i]))+data[i]
	red = False
	blue = False
	redS = "R" * K
	blueS= "B" * K
	
	for i in range(N):
		for j in range(N-K+1):
			s = ""
			for k in range(K):
				s += data[i][j+k]
			if s == redS: red = True
			if s == blueS: blue = True
	for i in range(N-K+1):
		for j in range(N):
			s = ""
			for k in range(K):
				s += data[i+k][j]
			if s == redS: red = True
			if s == blueS: blue = True
	for i in range(K-1,N):
		for j in range(N-K+1):
			s = ""
			for k in range(K):
				s += data[i-k][j+k]
			if s == redS: red = True
			if s == blueS: blue = True
	for i in range(N-K+1):
		for j in range(N-K+1):
			s = ""
			for k in range(K):
				s += data[i+k][j+k]
			if s == redS: red = True
			if s == blueS: blue = True
	if red and blue: return "Both"
	if red: return "Red"
	if blue: return "Blue"
	return "Neither"

for ii in range(test):
	(N, K) = map(int, f.readline().split())
	data = readn(f,N)
	print("Case #{0}: {1}".format(ii+1, solve(data, N, K)))