#!/usr/bin/python

def scal_prod(a, b):
	sum = 0
	for i in range(0, len(a)):
		sum = sum + a[i] * b[i]
	return sum

def perm(seq):
	if not seq:
		return [seq] # is an empty sequence
	else:
		temp = []
		for k in range(len(seq)):
			part = seq[:k] + seq[k+1:]
			for m in perm(part):
				temp.append(seq[k:k+1] + m)
		return temp

f = open("input.txt")

nl = '\n'

cases = int(f.readline().strip(nl))
i = 0
for i in range(0,cases):
	j = 0
	j = int(f.readline().strip(nl))
	a = f.readline().strip(nl).split(' ')
	b = f.readline().strip(nl).split(' ')

	na = []
	nb = []
	for item in a:
		na.append(int(item))
	for item in b:
		nb.append(int(item))
	
	alists = perm(na)
	sums = []
	for c in range(0,len(alists)):
		sums.append( scal_prod( alists[c], nb ) )
	ans = min(sums)
	output = "Case #" + str(i + 1) + ": " + str(ans)
	print output
