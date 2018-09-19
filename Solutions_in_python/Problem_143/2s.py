import sys

def sol(A, B, K):
	A = xrange(A)
	B = xrange(B)
	counter = 0
	for a in A:
		for b in B:
			if (a & b) < K:
				counter += 1

	return counter



fin  = open("B-small-attempt0.in", "r")
fout = open("output_2s.txt", "w")

case = int(fin.readline().strip())
for c in xrange(case):
	[A, B, K] = map(int, fin.readline().strip().split())
	fout.write("Case #" + str(c + 1) + ": " + str(sol(A, B, K)) + "\n")

fin.close()
fout.close()