def main():
	fin = open('A-large.in','r')
	fout = open('output.txt','w')
	
	T = int(fin.readline())
	
	for i in range(T):
		
		N,PD,PG = [int(x) for x in fin.readline().strip().split(' ')]
		
		pdPos = False
		pgPos = False
		
		g = gcd(PD,100)
		newPD = PD / g
		newDenom = 100 / g
		
		if (newDenom <= N):
			pdPos = True
		
		if (0 < PG < 100):
			pgPos = True
		elif (newPD == 0 and PG == 0 or newPD == newDenom and PG == 100):
			pgPos = True
		
		if (pdPos and pgPos):
			print 'Case #' + str(i+1) + ': Possible'
			fout.write('Case #' + str(i+1) + ': Possible' + '\n')
		else:
			print 'Case #' + str(i+1) + ': Broken'
			fout.write('Case #' + str(i+1) + ': Broken' + '\n')

def gcd(x,y):
	if y == 0:
		return x
	return gcd(y,x%y)

if __name__ == '__main__':
	main()
