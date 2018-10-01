
def main():
	solutions = []
	with open('A-large.in', 'r') as f:
		rows = int(f.readline())
		for i in xrange(rows):
			dn = f.readline()
			D = int(dn.split(' ')[0])
			N = int(dn.split(' ')[1])
			
			max_time = -1.0
			for j in xrange(N):
				ks = f.readline()
				K = int(ks.split(' ')[0])
				S = int(ks.split(' ')[1])
				time = float(D-K)/S
				if max_time < time:
					max_time = time
			
			sol = round(D/max_time, 6)
			solutions.append(sol)
			
	with open('A-large.out', 'w') as f:
		counter = 1
		for line in solutions:
			f.write("Case #{0}: {1}\n".format(str(counter), line))
			counter += 1

main()
