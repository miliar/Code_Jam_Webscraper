#!/usr/bin/python

import sys

def factor(n,P):
	res = []
	i=2
	while i<=n:
		already_added = False
		while i<=n and n%i==0:
			if not already_added:
				already_added = True
				if i>=P:
					res.append(i)
			n=n/i
		i+=1
	return set(res)

def handle_case(A,B,P):

	sets = []
	empty = 0
	for i in range(A,B+1):
		set = factor(i,P)
		if len(set)>0:
			sets.append(set)
		else:
			empty += 1

	i=0
	while(i<len(sets)):
		j=i+1
		had_intersection = 0
		sets_to_remove = []
		while (j<len(sets)):
			if len(sets[i].intersection(sets[j]))>0:
				sets[i] = sets[i].union(sets[j])
				sets_to_remove.append(sets[j])
				had_intersection = True
			j +=1

		for s in sets_to_remove:
			sets.remove(s)

		if not had_intersection:
			i += 1
	return len(sets)+empty

def main(filename):
	fsock = open(filename, "r")
	size = int(fsock.readline())
	for case in range(1,size+1):
		(A,B,P) = map(int,fsock.readline().rstrip("\n").split(" "))
		print "Case #%d: %d" % (case, handle_case(A,B,P))
	fsock.close()

if __name__ == "__main__":
	main(sys.argv[1])

