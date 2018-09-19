sample_input = """3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc"""

def get_paren_indices(s):
	result = {}
	in_paren = False
	start_paren = -1
	for i in xrange(len(s)):
		if s[i] == '(':
			in_paren = True
			start_paren = i
		elif s[i] == ')' and in_paren:
			in_paren = False
			result[start_paren] = i
		else:
			continue
	return result

class UnknownWord:
	def __init__(self, s):
		groups = get_paren_indices(s)
		self.my_list = []
		i = 0
		while i < len(s):
			if groups.has_key(i):
				substr = s[i+1:groups[i]]
				my_dict = {}
				for j in xrange(len(substr)):
					my_dict[substr[j]]=True
				self.my_list.append(my_dict)
				i += groups[i]-i+1
			else:
				self.my_list.append({s[i]: True})
				i += 1
	def determine_match(self, s):
		for i in xrange(len(s)):
			if not self.my_list[i].has_key(s[i]): return False
		return True
		

def process_input(input):
	input = input.split("\n")
	(l,d,n) = input[0].split()
	l=int(l)
	d=int(d)
	n=int(n)
	words={}
	for i in xrange(d):
		words[input[i+1]] = True
	for i in xrange(n):
		uw = UnknownWord(input[i+d+1])
		sum = 0
		for known_word in words:
			if uw.determine_match(known_word):
				sum += 1
		print("Case #%d: %d" % (i+1, sum))
		
f=open("A-large.in","r")
f=f.read()
process_input(f)

