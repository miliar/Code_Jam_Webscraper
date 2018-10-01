import re, sys

filename = sys.argv[1]

data = open(filename, 'r').read().splitlines()
params = data[0].split(" ")

N = params[0]

s0 = 'welcome to code jam'

S = []
for i in data[1:]:
	S += [i]
#print S

def foo(L, S):
	if len(L) == 0:
		if len(S) == 0:
			return 1
		else:
			return 0
	else:	
		if len(S) == 0:
			return 1
		else:
			if L[0] == S[0]:
				return	foo(L[1:], S[1:]) + foo(L[1:], S)
			else:
				return foo(L[1:], S)

#print foo(s2, s1)

idx = 0
for s in S:
	idx += 1
	matches = str(foo(s, s0))
	if len(matches) == 1:
		matches = '000' + matches
	if len(matches) == 2:
		matches = '00' + matches
	if len(matches) == 3:
		matches = '0' + matches
	if len(matches) > 4:
		matches = matches[-4:]
	print "Case #" + str(idx) + ": " +  matches
	