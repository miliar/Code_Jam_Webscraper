


f = open('B-small-attempt0.in', 'r')
wf = open('B-small-attempt0.out', 'w')



def doCase(case):
	C, F, X= [float(n) for n in f.readline().split()]
	base = 2
	time = 0
	#finish = [round(X/base, 7)]
	last = round(X/base, 7)
	bTime = 0
	while True:
		bTime += round(C/base, 7)
		base += F
		#finish.append(tmpTime)
		time = bTime + round(X/base, 7)
		if last <= time:
			break
		last = time
	wf.write('Case #{}: {}\n'.format(case, round(last, 7)))
	



def main():	
	N = int(f.readline())
	for i in range(1, N+1):
		doCase(i)
	f.close()
	wf.close()




if __name__ == '__main__':
	main()