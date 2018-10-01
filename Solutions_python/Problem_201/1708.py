infile = 'C-large.in'
outfile = 'cl.out'
import pdb
from collections import defaultdict

def main():
	with open(infile) as f, open(outfile, 'w+') as out:
		T = int(f.readline())
		for c in range(0, T):
			N, K = map(int, f.readline().split(" "))
			ma, mi = broombe(N, K)
			out.write('Case #{0}: {1} {2}\n'.format(c+1, ma, mi))		

def broom(n, k):
	print(n, k)
	tree = [n]
	for i in range(0, k - 1):
		po = tree.index(max(tree))
		c = tree.pop(po)
		if c % 2 == 0:
			tree.insert(po, int((c-1) / 2))
			tree.insert(po + 1, int((c-1) / 2) + 1)
		elif c % 2 == 1:
			tree.insert(po, int((c-1) / 2))
			tree.insert(po + 1, int((c-1) / 2))
	
	fin = max(tree)
	if fin % 2 == 0:
		return int((fin - 1) / 2) + 1, int((fin - 1) / 2)
	elif fin % 2 == 1:
		return int((fin - 1) / 2), int((fin - 1) / 2)
		
		
		
def broombe(n, k):
	kleft = k
	groups = defaultdict(int)
	groups[n] = 1
	while kleft > sum(groups.values()):
		ngroups = defaultdict(int)
		for g in groups:
			if g % 2 == 0: #an even makes an odd and an even
				ngroups[int((g-1) / 2)] += groups[g]
				ngroups[int((g-1) / 2) + 1] += groups[g]
					
			if g % 2 == 1: #an odd makes two evens
				ngroups[int((g-1) / 2)] += 2 * groups[g]
		
		kleft -= sum(groups.values())
		groups = ngroups
		assert len(groups) <= 2
	
	a = max(groups.keys())
	b = min(groups.keys()) 
	if len(groups) == 1:
		fin = a
	elif kleft <= groups[a]:
		fin = a
	elif kleft > groups[a]:
		fin = b
		
	if fin % 2 == 0:
		return int((fin - 1) / 2) + 1, int((fin - 1) / 2)
	elif fin % 2 == 1:
		return int((fin - 1) / 2), int((fin - 1) / 2)
		
				
if __name__=='__main__':
	main()

