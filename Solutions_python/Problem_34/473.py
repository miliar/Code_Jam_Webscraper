inp = """3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc"""
import re
exp = re.compile(r'\((\w+?)\)|(\w{1})')
inp = open("A-large.in", "r").read()
f2 = open("A-large.out", "w")


inp = inp.split('\n')
l, d, n = map(int, inp[0].split(' '))

inp = inp[1:]
tree = {}
for i in range(d):
	word = inp[i]
	
	prev = tree
	for c in word:
		if c not in prev:
			prev[c] = {}
			
		prev = prev[c]

def traverse(tree, letters):
	if not letters:
		return 1
	
	if len(letters[0]) > 1:
		res = 0
		for c in letters[0]:
			res += traverse(tree, [c] + letters[1:])
		return res
		
	if letters[0] in tree:
		return traverse(tree[letters[0]], letters[1:])
	else:
		return 0			
	

inp = inp[d:]
for i in range(n):
	letters = filter(lambda x: x, exp.split(inp[i]))
	print >> f2, "Case #%d: %d"%(i+1, traverse(tree, letters))
	