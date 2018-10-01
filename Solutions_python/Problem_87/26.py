from re import *
from sys import stderr
def readint():
	return int(raw_input())
def readfloat():
	return float(raw_input())
def readarray(N, foo=raw_input):
	return [foo() for i in xrange(N)]
def readlinearray(foo=int):
	return map(foo, raw_input().split())

def NOD(a, b):
	while b:
		a,b = b, a%b
	return a

def gen_primes(max):
	primes = [1]*(max+1)
	for i in range(2, max+1):
		if primes[i]:
			for j in range(i+i, max+1, i):
				primes[j] = 0
	primes[0] = 0
	primes[1] = 0
	return [x for x in range(max+1) if primes[x]]

def is_prime(N):
	i = 3
	if N == 1 or not(N % 2) and N != 2:
		return 0
	while i*i <= N:
		if not(N % i):
			return 0
		i += 2
	return 1

case_number = readint()
for case in xrange(case_number):
	X,S,R,t,N = readlinearray(float)
	N = int(N)
	ww = []
	for i in xrange(N):
		ww.append(readlinearray(float))
	if case == -1:
		print X,S,R,t,N
		print ww
		exit(0);
	lenghts1 = {}
	ss = 0.0
	for w in ww:
		l = w[1] - w[0]
		if w[2] not in lenghts1:
			lenghts1[w[2]] = 0.0
		lenghts1[w[2]] += l
		ss += l
	lenghts1[0] = X - ss
	time = 0.0
	for k in sorted(lenghts1.keys()):
		time_run = lenghts1[k] / (k + R)
		if time_run > t:
			time_run = t
		t -= time_run
		l = lenghts1[k]
		time += time_run
		l -= (k + R) * time_run
		time += l / (k + S)
	print "Case #%s: %.7lf" % (case + 1, time)
