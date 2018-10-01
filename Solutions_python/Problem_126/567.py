import sys
import itertools

T = int(sys.stdin.readline())

def solve(word, n):
	c = 0
	d = set()
	v = set( x for x in "aeiou")

	bC = cC = 0
	for i in range(0, len(word)):
		if word[i] not in v:
			if cC == 0:
				bC = i
			cC += 1

			if cC == n:
				for i in range(0, bC+1):
					for j in range(bC + n, len(word) + 1):
						if (i, j) not in d:
							c += 1
							d.add( (i, j) )

				bC += 1
				cC -= 1
		else:
			cC = bC = 0
	
	return c

for t in range(1, T+1):
	word, n = sys.stdin.readline().split()
	n = int(n)

	print("Case #%d: %d" % (t, solve(word, n)))





