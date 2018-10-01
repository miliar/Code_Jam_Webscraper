def warBitches():
	for i in range(input()):
		N = input()
		Naomi = [float(j) for j in raw_input().strip().split()]
		Ken = [float(j) for j in raw_input().strip().split()]
		Naomi.sort()
		Ken.sort()
		War(Naomi, Ken)
		print 'Case #%d: '%(i+1), BitchyWar(Naomi, Ken) , War(Naomi, Ken)
		

def War(Naomi, Ken):
	COUNT = 0
	I, J = 0, 0
	while I < len(Naomi):
		while J < len(Ken):
			if Ken[J] > Naomi[I]:
				COUNT += 1
				J += 1
				break
			else:
				J += 1
			
		I += 1
	return len(Naomi) - COUNT

def BitchyWar(Naomi, Ken):
	MAX = 0
	K = 0
	while K < len(Naomi):
		VAL = BWar(Naomi[K:], Ken[:(len(Naomi) - K)])
		if VAL > MAX:
			MAX = VAL
		K += 1
	return MAX

def BWar(Naomi, Ken):
	COUNT = 0
	for i in range(len(Naomi)):
		if Naomi[i] < Ken[i]:
			COUNT += 1
	return len(Naomi) - COUNT
	
	

if __name__ == '__main__':
	warBitches()
		
