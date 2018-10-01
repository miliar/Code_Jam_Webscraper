# Standing




def getMore(people):
	present = 0
	needed = 0
	for i,p in enumerate(people):
		if present < i:
			needed += i - present
			present += i - present
		present += p
	return needed


def to_int_list(s):
	s = s.replace('\n', '')
	return [int(i) for i in s]

output = "Case #{0}: {1}"

def next_case(s, i):
	s = s.split(" ")[-1]
	print output.format(i+1, getMore(to_int_list(s)))


def do_case(filename):
	f = open(filename,"r").readlines()
	cases = int(f[0])
	f = f[1:]
	for i in xrange(cases):
		next_case(f[i], i)




do_case("A-large.in")

