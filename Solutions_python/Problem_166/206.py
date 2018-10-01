import math
import itertools
from codejam import printCases
from codejam import Sort
from collections import Counter

result = []

def only_uniques(seq):
    return [k for k,n in Counter(seq).iteritems() if n == 1]

for case in range(input()):
	K,L,S = raw_input().split()
	K = int(K)
	L = int(L)
	S= int(S)
	keys = raw_input()
	target = raw_input()
	
	notinkeys = False
	total = 0 
	Max = 0
	prob = {}
	for i in range(len(keys)):
		if keys[i] not in prob:
			count = 0.
			for j in range(len(keys)):
				if keys[i] == keys[j]: count = count + 1
			prob[keys[i]] = float(count)/len(keys)
	#print prob
	#perms = list(itertools.permutations(keys, S))
	keys1 = []
	perms = []
	for letter in target:
		if letter not in keys:
			notinkeys = True
			break
	if notinkeys:
		result.append(0.0)	
		continue
	for i in range(len(keys)):
		if keys[i] not in keys1: keys1.append(keys[i])
	keys = ""
	for i in range(len(keys1)): keys = keys + keys1[i]
	perms = [p for p in itertools.product(keys, repeat=S)]
	for i in range(len(perms)):
		tmp = ""
		for j in range(len(perms[i])):
			tmp = tmp + perms[i][j]
		perms[i] = tmp
		
	#print perms
	for perm in perms:
		tr_count = 0
		for i in range(len(perm)-L+1):
			if perm[i:i+L] == target:
				#print perm[i:i+L]
				#print perm
				tr_count = tr_count + 1
		prod = 1
		Max = max(Max, tr_count)
		for letter in perm:
			prod = prod*prob[letter]
		total = total + prod*tr_count
	#print total
	result.append(Max - total)
printCases(result)
