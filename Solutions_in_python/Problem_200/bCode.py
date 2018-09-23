import sys

def num2array(i):
	s = str(i)
	tmp = []
	for c in s:
		tmp.append( int(c) )
	return tmp

def array2num(a):
	return int("".join(map(lambda i:str(i), a)))


def largestTidy(a):
	while True:
		tidy = True
		breaks_at = 0
		last = 0
		for i in range(len(a)):
			if a[i]<last:
				tidy = False
				breaks_at = i
				break
			last = a[i]

		if tidy:
			return a

		for i in range(breaks_at,len(a)):
			a[i] = 9

		a[breaks_at-1] -= 1


def process(i):
	return array2num(largestTidy(num2array(i)))


"""
inp = open("list.txt","r")

for line in inp:
	line = line.strip().split()
	num_in = int(line[0])
	num_out = int(line[1])

	calculated_out = process(num_in)
	print num_in, num_out, calculated_out
	assert calculated_out==num_out
"""
	
inp = open(sys.argv[1],"r")
inp.readline() # skip number of inputs

for i,s in enumerate(inp):
	num_in = int(s.strip())
	calculated_out = process(num_in)
	print "case #%i: %i"%( i+1, calculated_out)


#a = num2array(7326)
#print largestTidy(a)
