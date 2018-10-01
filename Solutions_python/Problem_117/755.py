import sys
import math
import re


def case():

	N, M = [int(x) for x in input().split(' ')]
	lawn = []
	maxH = []
	#print (N, M)

	for n in range(N):
		lawn.append([int(x) for x in input().split(' ')])
		maxH.append([100 for x in range(M)])

	#print (lawn)
	#print (maxH)

	for n in range(N):
		biggest = 0
		for h in lawn[n]:
			if h > biggest:
				biggest = h
		maxH[n] = [biggest for m in range(M)]
	#print (maxH)

	for m in range(M):
		biggest = 0
		for n in range(N):
			if lawn[n][m] > biggest:
				biggest = lawn[n][m]

		#print('big',biggest)
		for n in range(N):
			if maxH[n][m] > biggest:
				maxH[n][m] = biggest
	#print (maxH)

	for n in range(N):
		for m in range(M):
			if lawn[n][m] < maxH[n][m]:
				sys.stdout.write('NO')
				return

	sys.stdout.write('YES')





if __name__=="__main__":

	if len(sys.argv) > 1:
		sys.stdin = open(sys.argv[1])

	num_cases = int(input())

	for c in range (1, num_cases+1):
		sys.stdout.write('Case #')
		sys.stdout.write(str(c))
		sys.stdout.write(': ')
		case()
		sys.stdout.write('\n')
