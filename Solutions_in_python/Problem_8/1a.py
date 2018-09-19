#!/usr/bin/python

import sys, math

state = "init"
N = 1
case = 1
def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]



def solve(A, B, P):
	num = range(A,B+1)
	pr = [ n for n in primes(B) if n >= P ]
	#print pr
	cand = {}
	for p in pr:
		a = p
		while a <= B:
			if A <= a:
				try:
					cand[p].append(a)
				except KeyError:
					cand[p] = [a]

				try:
					num.remove(a)
				except ValueError:
					pass
			a += p

	#print cand

	sets = []
	#print num

	def myin(t, s):
		for i,k in enumerate(s):
			if t in k: return True, i

		return False, -1

	for k,v in cand.items():
		flag = False
		for t in v:
			a,b = myin(t, sets)
			if a:
				sets[b] += v
				flag = True
				break

		if not flag:
			sets.append(v)
#	if case==1:
#		for s in sets:
#			for a in s:
#				print a
#		for n in num:
#			print n
		#print sets
	return len(num) + len(sets)

for l in file(sys.argv[1]):
	l=l[:-1]
	if state=="init":
		N += int(l)
		state="case"
		case = 1
		continue

	if N==case: break

	if state=="case":
		c = l.split()
		r = solve(int(c[0]), int(c[1]), int(c[2]))
		#print l
		print "Case #%d: %d" % (case, r)
		case += 1


