fileName = 'B-large'


def main():
	solutions = []
	with open(fileName+'.in', 'r') as f:
		rows = int(f.readline())
		for i in xrange(rows):
			tc = f.readline()
			n = list(tc.strip())
			n = [int(i) for i in n]
			#print(n)
			sol = solve(n)
			solutions.append(int(''.join(map(str,sol))))
			
	with open(fileName+'.out', 'w') as f:
		counter = 1
		for line in solutions:
			f.write("Case #{0}: {1}\n".format(str(counter), line))
			counter += 1

def solve(n):
	done = False
	while(not done):
		done = True
		for i in xrange(len(n)-1):
			if n[i] > n[i+1]:
				if process(n, i):
					done = False
					break;
	n = purgeZeros(n)
	return n
	
def process(n, i):
	n[i] -= 1
	for j in xrange(i+1, len(n)):
		n[j] = 9
	if i > 0 and n[i] < n[i-1]:
		return True #needs to go from the start
	return False #can continue
	
def purgeZeros(n):
	counter = 0
	for i in n:
		if i == 0:
			counter += 1
		else:
			break
	return n[counter:]
main()

