


f = open('D-large.in', 'r')
wf = open('D-large.out', 'w')



def War(l1, l2):
	l1.sort()
	l2.sort()
	c= 0
	for i in l1:
		rm = 0
		for j in l2:
			if i < j:
				c += 1
				rm = j
				break
		if rm in l2:
			l2.remove(rm)
	return c
	
def DWar(l1, l2):
	l1.sort()
	l2.sort()
	c = 0
	for i in l1:
		rm = 0
		for j in l2:
			if i > j:
				c += 1
				rm = j
				break
		if rm in l2:
			l2.remove(rm)
	return c

def doCase(case):
	L = int(f.readline())
	Naomi = [float(n) for n in f.readline().split()]
	Ken = [float(n) for n in f.readline().split()]
	dpNaomi = DWar(list(Naomi), list(Ken))
	pNaomi = L - War(list(Naomi), list(Ken))
	wf.write('Case #{}: {} {}\n'.format(case, dpNaomi, pNaomi))

def main():	
	N = int(f.readline())
	for i in range(1, N+1):
		doCase(i)
	f.close()
	wf.close()




if __name__ == '__main__':
	main()