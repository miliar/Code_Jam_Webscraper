#!/usr/bin/env python
fin = open('d.in','r')
fout = open('d.out','w')

def main():
	global fin, fout
	T = int(fin.readline())
	for test in range(T):
		n = int(fin.readline())
		a = [int(i) for i in fin.readline().split()]
		for i in range(len(a)):
			a[i] -= 1
		solve(test, a)

def fact(n):
	s = 1.0
	for i in range(2, n + 1):
		s *= i
#	p = 1.0 / s
#	s = 0.0
#for i in range(1, 1000):
#		v = i * ((1 - p)** (i - 1)) * p
#		s += v
#print s
	return s

def solve(T, a):
	global fout
	n = len(a)
	sol = 0
	use = [0 for i in range(n + 1)]
	for i in range(len(a)):
		if a[i] != i and use[i] == 0:
			j = a[i]
			use[j] = 1
			nr = 1
			while j != i:
				j = a[j]
				use[j] = 1
				nr += 1
			sol += nr
	sol = round(sol, 20)
	sol = str(sol)
	if 'e' in sol:
		while sol[-1] != 'e':
			sol = sol[:-1]
		sol = sol[:-1]		
	fout.write( 'Case #' + str(T+1) + ': ' + str(sol)+'\n')

if __name__ == '__main__':
	main()
