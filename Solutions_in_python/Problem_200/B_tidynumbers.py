def shape(a):
	i = 0
	while a[i] == '0' and i < len(a):
		i += 1
	a = a[i:len(a)]
	a = ''.join(a)
	return a

def subtract(a, p):
	while p >= 0:
		if a[p] != '0':
			a[p] = str(int(a[p]) -1)
			break
		else:
			a[p] = '9'
			p -= 1
	return a

def update(a, p):
	for i in range(p+1, len(a)):
		a[i] = '9'
	while int(a[p]) < int(a[p-1]) and p > 0:
		a[p] = '9'
		a = subtract(a, p-1)
		p -= 1
	return a

if __name__ == '__main__':
	N = input()
	a = []
	for i in range(N):
		a = list(raw_input())
		l = len(a)
		x = 0
		for j in range(l):
			if int(a[j]) < x:
				a = update(a,j)
				break
			else:
				x = int(a[j])
		a = shape(a)	
		output = 'Case #' + str(i+1) + ': ' + a
		print output
