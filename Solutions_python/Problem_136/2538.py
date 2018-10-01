import sys
import itertools


def main():
	file = sys.stdin
	lines = iter(file.readlines())
	
	testCases = int(lines.next())
	caseNo = itertools.count(1)
	
	while testCases:
		C, F, X = map(float, lines.next().rstrip().lstrip().split(' '))
		#print C, F, X
		n =2.
		if X<C:
			print 'Case #%d: %.7f' %(caseNo.next(), X/n)
		else:
			prev_optimum_time, optimum_time = X/n, X/n
			sum_time = 0
			while(1):
				farm_time = C/n
				n += F
				finish_time = X/n
				
				
				sum_time  += farm_time
				prev_optimum_time = optimum_time
				optimum_time = sum_time + finish_time
				#print farm_time, optimum_time
				if (prev_optimum_time< optimum_time):
					print 'Case #%d: %.7f' %(caseNo.next(), prev_optimum_time)
					break
				
				
				
				
		testCases -= 1

if __name__ == '__main__' :
	main()
	