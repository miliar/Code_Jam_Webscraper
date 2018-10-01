#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
from math import sqrt

class Group:
	def __init__(self, id):
		self.id = id
		
limit = 1000000
is_primes = [ True for i in range(0, limit) ]
factors = [ [] for i in range(0, limit) ]

i = 2
count = 0
primes = []
while i < limit:
	if is_primes[i]:
		factors[i].append(i)
		primes.append(i)
		j = i+i
		while j < limit:
			is_primes[j] = False
			factors[j].append(i)
			j = j+i
			
	i = i+1

def get_factors(number):
	global limit, primes
	if number < limit:
		return factors[number]

	l = sqrt(number) + 1
	i = 2
	result = []
	
	cur = 0
	while i < l:
		if is_primes[i] and number%i==0:
			result.append(i)
			j = number / i
			if j > l:
				result.append(j)
		i = i+1
		
	result.sort()
	return result
	
def main():
	
	fi = sys.stdin
	case = 0
	for line in fi:
		tmps = line.strip().split(' ')
		if len(tmps)!=3:
			continue
			
		case = case+1
			
		a = int(tmps[0])
		b = int(tmps[1])
		p = int(tmps[2])
		groups = {} 
		
		number = a
		while number <= b:
			last_group = None
			facts = get_factors(number)
			for factor in facts:
				if factor >= p:
					if factor not in groups:
						groups[factor] = Group(id=factor)
					
					if last_group is not None:
						groups[factor] = last_group
					last_group = groups[factor]
					
			if last_group is None:
				groups[number] = Group(id=number)
			number = number+1

		ans = {}
		for factor, group in groups.items():
			ans[group.id] = group 
			
		result = len(ans)
		print "Case #%(case)d: %(result)d" % locals()

	pass
	
if __name__ == '__main__':
	sys.exit(main())


